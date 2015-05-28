# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_problem_saved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('oname', models.CharField(max_length=128)),
                ('problem', models.ForeignKey(to='builder.Problem')),
            ],
        ),
    ]
