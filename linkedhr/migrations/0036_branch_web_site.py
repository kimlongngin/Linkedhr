# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0035_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='web_site',
            field=models.CharField(default=datetime.datetime(2018, 5, 7, 11, 33, 4, 868588, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
