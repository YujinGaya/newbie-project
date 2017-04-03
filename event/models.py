import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    time = models.DateTimeField('When event holds')
    registered = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField()
