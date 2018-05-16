# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0007_auto_20180427_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_recruit',
            field=models.CharField(max_length=10, choices=[(b'1', b'Recruitor'), (b'2', b'Job Finder')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
