# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0030_auto_20180506_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='google_map',
        ),
        migrations.AddField(
            model_name='company',
            name='is_branch',
            field=models.BooleanField(default=False, verbose_name=b'Does your company has more than one branch ?'),
        ),
    ]
