# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0014_auto_20180502_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=10, verbose_name=b'What will you do ?', choices=[(b'1', b'POS_DOC'), (b'2', b'PHD'), (b'3', b'MS'), (b'4', b'BC'), (b'5', b'Other')]),
        ),
    ]
