# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_auto_20180610_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='name',
            new_name='title',
        ),
    ]
