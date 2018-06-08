# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0060_auto_20180607_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(default=datetime.datetime(2018, 6, 8, 15, 2, 44, 635430, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
