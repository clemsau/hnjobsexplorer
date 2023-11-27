from django.db import models


class Thread(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Job(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    body = models.TextField()
    deactivated = models.BooleanField(default=False)
    seen = False
