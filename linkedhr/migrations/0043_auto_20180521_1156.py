# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0042_auto_20180519_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=datetime.datetime(2018, 5, 21, 11, 56, 14, 23711, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(default=datetime.datetime(2018, 5, 21, 11, 56, 21, 760813, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='present_address',
            field=models.CharField(default=datetime.datetime(2018, 5, 21, 11, 56, 33, 146048, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_recruit',
            field=models.CharField(max_length=10, verbose_name=b'What will you do ?', choices=[(b'1', b'Recruiter'), (b'2', b'Seeker')]),
        ),
    ]
