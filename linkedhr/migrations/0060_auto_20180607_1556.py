# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0059_auto_20180602_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitmentbranch',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='graduation_at',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Graduation at'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_education_at',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Start at'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
    ]
