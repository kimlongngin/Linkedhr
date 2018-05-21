# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0043_auto_20180521_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='present_address',
            field=models.TextField(),
        ),
    ]
