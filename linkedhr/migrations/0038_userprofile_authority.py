# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0037_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='authority',
            field=models.BooleanField(default=False),
        ),
    ]
