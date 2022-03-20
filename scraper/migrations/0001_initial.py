from django.db import migrations
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from scraper.tasks.news_fetch import initiate_fetch

FETCH_NEWS_TASK_SPEC = {
    "name": "Task for fetching news periodically.",
    "task": "scraper.tasks.news_fetch.initiate_fetch",
}


def fetch_news_schedule(apps, schema_editor):
    schedule = CrontabSchedule.objects.create(minute=5)
    PeriodicTask.objects.create(crontab=schedule, **FETCH_NEWS_TASK_SPEC)


def initial_fetch(apps, schema_editor):
    initiate_fetch()


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fetch_news_schedule),
        migrations.RunPython(initial_fetch)
    ]
