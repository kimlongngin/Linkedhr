# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0013_auto_20180502_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='date_graduation',
            new_name='graduation_at',
        ),
        migrations.AddField(
            model_name='education',
            name='start_education_at',
            field=models.DateField(default=datetime.date.today, blank=True),
        ),
    ]
