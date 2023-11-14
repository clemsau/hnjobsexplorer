from django.views.generic import TemplateView

from .models import Thread, Job


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["threads"] = Thread.objects.all()
        context["jobs"] = Job.objects.all()[0:30]

        return context
