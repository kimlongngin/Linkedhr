# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0050_auto_20180530_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(to='linkedhr.City'),
        ),
    ]
