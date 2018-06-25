# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-25 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkedhr', '0075_recruitment_count_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobtype_of', to='linkedhr.JobType'),
        ),
    ]
