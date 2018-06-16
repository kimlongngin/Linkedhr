# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-14 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import linkedhr.models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0062_auto_20180610_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_logo',
            field=models.ImageField(blank=True, height_field=b'height_field', null=True, upload_to=linkedhr.models.upload_location, width_field=b'width_field'),
        ),
    ]
