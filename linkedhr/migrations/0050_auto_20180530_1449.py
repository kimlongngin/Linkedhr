# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0049_auto_20180530_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='company',
            new_name='com_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(related_name='user_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
