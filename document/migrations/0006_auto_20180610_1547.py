# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_auto_20180610_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='user_id',
            new_name='user',
        ),
    ]
