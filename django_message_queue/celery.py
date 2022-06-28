from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_message_queue.settings')

app = Celery('django_message_queue')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    # prints all the metadata about the request
    print('Request: {0!r}'.format(self.request))

# to run this func in python console in ide
# python manage.py shell in manage.py directory
# from django_message_queue.celery import debug_task
# debug_task.delay() #.delay() to tell Celery to add the task to the queue.
# celery -A django_message_queue.celery worker --loglevel=info