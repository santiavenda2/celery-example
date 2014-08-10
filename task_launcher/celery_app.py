from __future__ import absolute_import

from celery import Celery

app = Celery('celery_app',
             broker='amqp://',
             backend='amqp://',
             include=['task_launcher.tasks'])

app.config_from_object('task_launcher.celeryconfig')

if __name__ == '__main__':
    app.start()
