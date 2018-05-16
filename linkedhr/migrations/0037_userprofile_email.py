# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0036_branch_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default=datetime.datetime(2018, 5, 8, 13, 25, 30, 93936, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
