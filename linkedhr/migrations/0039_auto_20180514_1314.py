# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('linkedhr', '0038_userprofile_authority'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_experience', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(related_name='experience_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_status',
            field=models.BooleanField(default=True),
        ),
    ]
