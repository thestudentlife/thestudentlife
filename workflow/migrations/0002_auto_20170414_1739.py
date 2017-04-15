# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(max_length=256, default='author', choices=[('chief_editor', 'Editor-in-Chief'), ('administrator', 'Administrator'), ('web_developer', 'Web Developer'), ('editor', 'Section Editor'), ('author', 'Author'), ('guest', 'Guest Author'), ('photographer', 'Photographer'), ('graphic_designer', 'Graphic Designer')]),
        ),
    ]
