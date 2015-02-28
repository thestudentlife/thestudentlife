# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='credit',
            field=models.ForeignKey(to='workflow.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='frontarticle',
            name='article',
            field=models.OneToOneField(to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carouselarticle',
            name='article',
            field=models.OneToOneField(to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='workflow.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(to='mainsite.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(related_name='articles', to='mainsite.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='subsections',
            field=models.ManyToManyField(to='mainsite.Subsection', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='article',
            field=models.ForeignKey(to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='mainsite.Photo'),
            preserve_default=True,
        ),
    ]
