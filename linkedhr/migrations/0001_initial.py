# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('city_logo', models.FileField(upload_to=b'')),
                ('description', models.TextField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=150)),
                ('company_logo', models.FileField(upload_to=b'')),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('google_map', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(to='linkedhr.City')),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(to='linkedhr.City')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('degree', models.CharField(max_length=150)),
                ('institute', models.CharField(max_length=150)),
                ('date_graduation', models.DateField(default=datetime.date.today, blank=True)),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=50)),
                ('Company', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today, blank=True)),
                ('due_date', models.DateField(default=datetime.date.today, blank=True)),
                ('document', models.FileField(upload_to=b'')),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('salary', models.CharField(max_length=30)),
                ('number_of_employee', models.IntegerField(default=0)),
                ('experience', models.CharField(max_length=30)),
                ('start_date', models.DateField(default=datetime.date.today, blank=True)),
                ('due_date', models.DateField(default=datetime.date.today, blank=True)),
                ('job_requirement', models.TextField()),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('is_status', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='RecruitmentBranch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(to='linkedhr.Branch')),
                ('company', models.ForeignKey(to='linkedhr.Company')),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='SkillList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.CharField(max_length=4)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_status', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=7)),
                ('date_of_birth', models.DateField(default=datetime.date.today, blank=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_recruit', models.CharField(max_length=2)),
                ('is_status', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(to='linkedhr.City')),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Villege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(to='linkedhr.District')),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_list',
            field=models.ForeignKey(to='linkedhr.SkillList'),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='Branch',
            field=models.ForeignKey(to='linkedhr.RecruitmentBranch'),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='company',
            field=models.ForeignKey(to='linkedhr.Company'),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='job_type',
            field=models.OneToOneField(related_name='jobtype_of', to='linkedhr.JobType'),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='position',
            field=models.ForeignKey(to='linkedhr.Position'),
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(to='linkedhr.Company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='location',
            field=models.ForeignKey(to='linkedhr.City'),
        ),
        migrations.AddField(
            model_name='apply',
            name='position',
            field=models.ForeignKey(to='linkedhr.Recruitment'),
        ),
        migrations.AddField(
            model_name='apply',
            name='stage',
            field=models.ForeignKey(to='linkedhr.Stage'),
        ),
    ]
