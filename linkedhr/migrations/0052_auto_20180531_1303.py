# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0051_auto_20180531_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
