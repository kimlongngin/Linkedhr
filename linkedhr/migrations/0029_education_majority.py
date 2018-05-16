# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0028_auto_20180506_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='majority',
            field=models.CharField(default=datetime.datetime(2018, 5, 6, 8, 30, 1, 235562, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
