from django.core.management.base import BaseCommand, CommandError

import requests

from jobs.constants import HN_WHOISHIRING_POSTS_URL, HN_ITEM_URL
from jobs.models import Thread


class Command(BaseCommand):
    help = 'Fetches latest thread from the whoishiring user'

    def handle(self, *args, **options):
        try:
            response = requests.get(HN_WHOISHIRING_POSTS_URL)
            if response.status_code != 200:
                raise CommandError('Unable to fetch latest thread')

            submitted = response.json()['submitted']
            for thread_id in submitted[:3]:
                response = requests.get(HN_ITEM_URL.format(thread_id))
                if response.status_code != 200:
                    raise CommandError('Unable to fetch latest thread')

                title = response.json()['title']
                if 'who is hiring' in title.lower():
                    thread, created = Thread.objects.get_or_create(id=thread_id)
                    if not created:
                        continue

                    thread.title = title
                    thread.date = title[title.find('(') + 1:title.find(')')]
                    thread.save()
                    continue

        except Exception as e:
            raise CommandError('Unable to fetch latest thread: {}'.format(e))
