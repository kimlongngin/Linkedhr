# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-23 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0071_auto_20180623_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruitment',
            old_name='Branch',
            new_name='branch',
        ),
    ]
