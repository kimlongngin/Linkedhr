# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0058_auto_20180601_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
