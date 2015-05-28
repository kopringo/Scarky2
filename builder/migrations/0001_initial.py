# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=32)),
                ('version', models.CharField(max_length=32)),
                ('remote_id', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=8)),
                ('date', models.DateTimeField()),
                ('remote_code', models.CharField(max_length=32)),
                ('secret', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('input', models.FileField(upload_to=b'uploaded')),
                ('output', models.FileField(upload_to=b'uploaded')),
                ('rank', models.CharField(max_length=16, choices=[(b'bin-date', b'Binary by date'), (b'bin-time', b'Binary by time'), (b'bin-source', b'Binary by length of source code')])),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_stop', models.DateTimeField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('resource', models.CharField(max_length=128, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('stats_visits', models.IntegerField(default=0)),
                ('stats_submissions', models.IntegerField(default=0)),
                ('languages', models.ManyToManyField(to='builder.Language')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('status', models.IntegerField(default=0)),
                ('time', models.FloatField(default=0.0)),
                ('mem', models.IntegerField(default=0)),
                ('remote_id', models.IntegerField(default=0)),
                ('language', models.ForeignKey(to='builder.Language')),
                ('problem', models.ForeignKey(to='builder.Problem')),
            ],
        ),
    ]
