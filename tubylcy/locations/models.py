from django.db import models
from django.contrib.auth.models import User, Group


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    address = models.TextField()

    # some kind of geohash?
    localization = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
