# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0053_auto_20180531_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 6, 1, 11, 36, 48, 74500, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(default=datetime.datetime(2018, 6, 1, 11, 36, 58, 690626, tzinfo=utc), max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='present_address',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
