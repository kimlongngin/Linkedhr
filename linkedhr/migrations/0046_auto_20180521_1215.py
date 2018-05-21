# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0045_auto_20180521_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='present_address',
            field=models.CharField(max_length=100),
        ),
    ]
