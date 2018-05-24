# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0046_auto_20180521_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.OneToOneField(to='linkedhr.City'),
        ),
    ]
