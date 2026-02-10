import os
from celery import Celery
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = (

    "run-every-24-hours": {
        "task": "check_overdue_loans",
        "schedule": timedelta(days=1)
    },
)
