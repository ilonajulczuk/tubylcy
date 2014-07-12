from django.db import models
from django.contrib.auth.models import User, Group


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    address = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    # some kind of geohash?
    localization = models.CharField(max_length=100)
    creator = models.ForeignKey(User)


class Quest(models.Model):
    created = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(null=True)
    bounty = models.FloatField(default=0)

    title = models.CharField(max_length=200)
    description = models.TextField()

    assignees = models.ManyToManyField(User, related_name='assigned_quests')
    reporter = models.ForeignKey(User, related_name='reported_quests')