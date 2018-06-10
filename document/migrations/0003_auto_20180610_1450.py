# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import document.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0002_auto_20180610_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to=document.models.content_file_name)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_status', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(related_name='documentuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.RemoveField(
            model_name='document',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
