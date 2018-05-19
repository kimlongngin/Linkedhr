# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0040_auto_20180514_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(related_name='user_company', to='linkedhr.UserProfile'),
        ),
    ]
