# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-09 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ms_type', models.CharField(choices=[('1', 'user-admin'), ('2', 'seeker-recruitor'), ('3', 'recruitor-seeker')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='room',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='messagetype',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_message_type', to='chat.Message'),
        ),
    ]
