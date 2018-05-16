# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0011_auto_20180429_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='user_id',
            field=models.OneToOneField(related_name='user_education', to='linkedhr.UserProfile'),
        ),
    ]
