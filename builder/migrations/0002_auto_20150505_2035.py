# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='date_stop',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
