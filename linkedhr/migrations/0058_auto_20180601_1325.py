# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0057_auto_20180601_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.FileField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='web_site',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
