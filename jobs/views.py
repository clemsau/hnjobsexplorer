from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import ContextMixin

from .models import Thread, Job


class IndexView(View, ContextMixin):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["threads"] = Thread.objects.all()
        context["jobs"] = Job.objects.filter(thread=kwargs["current_thread_id"])
        return context

    def get(self, request, *args, **kwargs):
        kwargs["current_thread_id"] = "0"
        if Thread.objects.last():
            kwargs["current_thread_id"] = Thread.objects.last().id
        return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        kwargs["current_thread_id"] = request.POST["current_thread_id"]
        context = self.get_context_data(**kwargs)
        context["jobs"] = context["jobs"].filter(body__icontains=request.POST["search"])
        return render(request, "components/listing.html", context)
