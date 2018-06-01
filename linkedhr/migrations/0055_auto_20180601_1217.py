# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import linkedhr.models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0054_auto_20180601_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.FileField(upload_to=linkedhr.models.user_directory_path),
        ),
    ]
