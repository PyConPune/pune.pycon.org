from celery import Celery

import logging

import settings

_log = logging.getLogger(__name__)


if settings.CELERY_BROKER_URL:
    broker_url = settings.CELERY_BROKER_URL
else:
    broker_url = 'amqp://localhost:5672'

app = Celery('tasks', broker=broker_url)


@app.task()
def send_mail():
    ''' Send the emails in an async manner '''
    print 'Sending mails bro'
