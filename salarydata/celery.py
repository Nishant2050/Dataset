import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salarydata.settings')

app = Celery('salarydata')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()