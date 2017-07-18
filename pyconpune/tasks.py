import os
from celery import Celery

import logging
_log = logging.getLogger(__name__)


if os.environ.get('CELERY_BROKER_URL'):
    broker_url = os.environ['CELERY_BROKER_URL']
else:
    broker_url = 'amqp://pycon:pycon@localhost/pycon_vhost'

app = Celery('tasks', broker=broker_url, backend=broker_url)


@app.task()
def send_mail():
    ''' Send the emails in an async manner '''
    print 'Sending mails bro'

