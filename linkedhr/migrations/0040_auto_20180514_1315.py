# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0039_auto_20180514_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencecheck',
            name='is_experience',
            field=models.BooleanField(default=False),
        ),
    ]
