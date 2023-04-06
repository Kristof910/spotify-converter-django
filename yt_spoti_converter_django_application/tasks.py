from celery import shared_task
from .converter.converting_manager import converting_manager


@shared_task
def tasks(request):
    converting_manager(request)
