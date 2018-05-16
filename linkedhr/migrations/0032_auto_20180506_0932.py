# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0031_auto_20180506_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_status',
            field=models.BooleanField(default=False),
        ),
    ]
