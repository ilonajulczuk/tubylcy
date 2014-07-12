# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('address', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('localization', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('finished', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('assignees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
