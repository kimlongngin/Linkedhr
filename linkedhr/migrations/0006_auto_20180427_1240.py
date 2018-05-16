# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0005_auto_20180427_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.ForeignKey(default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
        ),
    ]
