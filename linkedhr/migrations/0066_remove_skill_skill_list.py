# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-17 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0065_auto_20180617_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_list',
        ),
    ]