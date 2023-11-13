from django.contrib import admin

# Register your models here.

from .models import Thread, Job

admin.site.register(Thread)
admin.site.register(Job)