# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0024_auto_20180505_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(related_name='companyuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
