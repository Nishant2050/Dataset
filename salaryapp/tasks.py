from celery import shared_task
from .models import Data


@shared_task
def dataset():
    data = Data.objects.all()
    print('shared data', data)
    return data