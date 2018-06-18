# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-18 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import linkedhr.models


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0067_auto_20180618_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.FileField(blank=True, upload_to=linkedhr.models.user_directory_path, validators=[linkedhr.models.validate_file_extension]),
        ),
    ]