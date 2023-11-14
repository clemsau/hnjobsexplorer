# Generated by Django 4.2.5 on 2023-11-13 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Thread",
            fields=[
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=100)),
                ("date", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("body", models.TextField()),
                (
                    "thread",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.thread"
                    ),
                ),
            ],
        ),
    ]