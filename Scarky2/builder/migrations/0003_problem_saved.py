# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20150505_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='saved',
            field=models.BooleanField(default=False),
        ),
    ]
