BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TRACK_STARTED = True

# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
# CELERY_TIMEZONE = 'Europe/Oslo'
# CELERY_ENABLE_UTC = True