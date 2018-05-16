# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0017_auto_20180503_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='user_id',
            field=models.ForeignKey(related_name='stageuserprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
