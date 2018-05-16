# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0033_auto_20180506_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='company',
            new_name='company_id',
        ),
        migrations.AddField(
            model_name='company',
            name='web_site',
            field=models.CharField(default=datetime.datetime(2018, 5, 7, 11, 10, 9, 893899, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
