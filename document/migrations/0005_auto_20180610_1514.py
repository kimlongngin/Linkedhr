# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import document.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_auto_20180610_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.FileField(upload_to=document.models.content_file_name),
        ),
    ]
