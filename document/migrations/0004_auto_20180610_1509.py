# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20180610_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
