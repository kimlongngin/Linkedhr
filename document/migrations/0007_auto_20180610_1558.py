# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_auto_20180610_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='title',
            new_name='name',
        ),
    ]
