# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0047_auto_20180524_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='company_id',
            new_name='com_id',
        ),
    ]
