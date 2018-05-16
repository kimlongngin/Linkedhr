# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0029_education_majority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='Company',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='education',
            name='graduation_at',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Graduation at', blank=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_education_at',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Start at', blank=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user_id',
            field=models.ForeignKey(related_name='user_experience', to=settings.AUTH_USER_MODEL),
        ),
    ]
