# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0020_auto_20180504_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 5, 4, 9, 13, 58, 37117, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
