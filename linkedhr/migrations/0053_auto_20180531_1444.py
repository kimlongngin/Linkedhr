# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0052_auto_20180531_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='present_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
