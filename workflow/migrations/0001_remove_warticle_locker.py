# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', 'data_migration_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warticle',
            name='locker',
        ),
    ]
