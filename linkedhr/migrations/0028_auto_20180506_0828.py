# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0027_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user_id',
            field=models.ForeignKey(related_name='user_education', to=settings.AUTH_USER_MODEL),
        ),
    ]
