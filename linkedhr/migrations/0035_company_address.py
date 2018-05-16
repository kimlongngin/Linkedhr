# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0034_auto_20180507_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=datetime.datetime(2018, 5, 7, 11, 30, 58, 778804, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
