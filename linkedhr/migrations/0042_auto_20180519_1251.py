# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0041_auto_20180519_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(related_name='user_company', to=settings.AUTH_USER_MODEL),
        ),
    ]
