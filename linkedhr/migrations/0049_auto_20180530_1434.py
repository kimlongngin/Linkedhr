# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0048_auto_20180524_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='com_id',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
