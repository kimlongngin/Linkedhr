# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0008_auto_20180428_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_recruit',
            field=models.CharField(max_length=10, verbose_name=b'What will you do ?', choices=[(b'1', b'Recruitor'), (b'2', b'Job Finder')]),
        ),
    ]
