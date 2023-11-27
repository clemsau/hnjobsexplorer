from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("seen", views.SeenJob.as_view(), name="seen"),
    path("reset_seen", views.ResetSeenJob.as_view(), name="reset_seen"),
]