from django.core.management.base import BaseCommand, CommandError

import requests

from jobs.constants import HN_ITEM_URL
from jobs.models import Thread, Job


class Command(BaseCommand):
    help = 'Fetches latest jobs from the last thread'

    def handle(self, *args, **options):
        try:
            latest_threads = Thread.objects.all().order_by('timestamp')[:2]
            for latest_thread in latest_threads:
                response = requests.get(HN_ITEM_URL.format(latest_thread.id))
                if response.status_code != 200:
                    raise CommandError('Unable to fetch latest jobs')

                kids = set(response.json()['kids'])
                saved_kids = set(map(int, [job.id for job in latest_thread.job_set.all()]))

                for job_id in (kids - saved_kids):
                    job, created = Job.objects.get_or_create(id=job_id, thread=latest_thread)
                    if not created:
                        continue

                    response = requests.get(HN_ITEM_URL.format(job_id))
                    if response.status_code != 200:
                        raise CommandError('Unable to fetch latest jobs')

                    job.body = response.json().get('text', '')
                    if not job.body:
                        job.deactivated = True

                    job.save()

        except Exception as e:
            raise CommandError('Unable to fetch latest jobs: {}'.format(e))
