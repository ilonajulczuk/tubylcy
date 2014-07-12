# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20140712_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='bounty',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
