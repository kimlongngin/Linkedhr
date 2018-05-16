# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0025_auto_20180505_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='user_id',
            field=models.ForeignKey(related_name='user_document', to='linkedhr.UserProfile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user_id',
            field=models.ForeignKey(related_name='user_experience', to='linkedhr.UserProfile'),
        ),
    ]
