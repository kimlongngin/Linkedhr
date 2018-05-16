# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkedhr', '0021_education_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to=b'')),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(related_name='user_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='experience',
            name='document',
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(default=datetime.datetime(2018, 5, 4, 9, 29, 28, 874168, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='is_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user_id',
            field=models.ForeignKey(related_name='user_experience', to=settings.AUTH_USER_MODEL),
        ),
    ]
