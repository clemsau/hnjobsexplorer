# Generated by Django 4.2.5 on 2023-11-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="deactivated",
            field=models.BooleanField(default=False),
        ),
    ]
