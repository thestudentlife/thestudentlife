# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='section',
            field=models.ForeignKey(to='mainsite.Section', related_name='articles'),
            preserve_default=True,
        ),
    ]
