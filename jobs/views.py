from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import ContextMixin

from .models import Thread, Job


class IndexView(View, ContextMixin):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["threads"] = Thread.objects.all()
        context["jobs"] = Job.objects.filter(thread=kwargs["current_thread_id"], deactivated=False)
        context["jobs"] = set_seen_jobs(context["jobs"], self.request.session.get("seen_jobs", {}))
        context["jobs_count"] = len(context["jobs"])
        return context

    def get(self, request, *args, **kwargs):
        kwargs["current_thread_id"] = "0"
        if Thread.objects.last():
            kwargs["current_thread_id"] = Thread.objects.last().id

        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        kwargs["current_thread_id"] = request.POST["current_thread_id"]
        context = self.get_context_data(**kwargs)
        keywords = request.POST["search"].strip().split(",")

        if len(keywords) > 3:
            keywords = keywords[:3]

        for keyword in keywords:
            context["jobs"] = context["jobs"].filter(body__icontains=keyword)

        context["jobs"] = set_seen_jobs(context["jobs"], self.request.session.get("seen_jobs", {}))
        if request.POST.get("hideSeed"):
            for job in context["jobs"]:
                if job.seen:
                    context["jobs"] = context["jobs"].exclude(id=job.id)

        context["jobs_count"] = len(context["jobs"])
        return render(request, "components/listing.html", context)


class SeenJob(View):
    def post(self, request, *args, **kwargs):
        seen = request.POST["seen"]
        request.session["seen_jobs"] = request.session.get("seen_jobs", {})
        request.session["seen_jobs"][seen] = True
        return HttpResponse(status=200)


class ResetSeenJob(View):
    def get(self, request, *args, **kwargs):
        request.session["seen_jobs"] = {}
        return redirect("index")


def set_seen_jobs(jobs, seen_jobs):
    if not seen_jobs:
        return jobs

    for job in jobs:
        job.seen = seen_jobs.get(job.id, False)
    return jobs
