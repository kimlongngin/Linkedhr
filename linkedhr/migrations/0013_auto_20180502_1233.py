# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0012_auto_20180502_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user_id',
            field=models.ForeignKey(related_name='user_education', to='linkedhr.UserProfile'),
        ),
    ]
