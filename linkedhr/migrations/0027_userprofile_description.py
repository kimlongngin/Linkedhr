# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0026_auto_20180505_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 5, 6, 8, 5, 55, 24223, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
