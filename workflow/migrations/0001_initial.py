# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('photo', 'Photo Assignment'), ('article', 'Article Assignment')], default='photo_assignment', max_length=50)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('accepted', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('position', models.CharField(choices=[('chief_editor', 'Editor-in-Chief'), ('administrator', 'Administrator'), ('web_developer', 'Web Developer'), ('editor', 'Section Editor'), ('author', 'Author'), ('guest', 'Guest Author'), ('photographer', 'Photographer'), ('graphic_designer', 'Graphic Designer')], default='author', max_length=50)),
                ('display_name', models.CharField(max_length=50, blank=True)),
                ('legacy_id', models.PositiveIntegerField(null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('reviewer', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('article', models.ForeignKey(to='mainsite.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('editor', models.ForeignKey(to='workflow.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='WArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.TextField()),
                ('article', models.OneToOneField(to='mainsite.Article')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(to='workflow.Profile', related_name='assignment_received'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(null=True, to='mainsite.Article', related_name='assignment'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(null=True, to='mainsite.Photo', related_name='assignment'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='sender',
            field=models.ForeignKey(to='workflow.Profile', related_name='assignment_created'),
        ),
    ]
