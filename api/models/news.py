import uuid

from django.db import models

from api.constants.news import RSS_FEED_TYPES


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    symbol = models.IntegerField(choices=RSS_FEED_TYPES)
