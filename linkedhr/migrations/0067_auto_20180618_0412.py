# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-18 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0066_remove_skill_skill_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='skilllist',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
