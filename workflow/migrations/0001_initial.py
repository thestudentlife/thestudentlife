# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('photo', 'Photo Assignment'), ('article', 'Article Assignment')], max_length=50, default='photo_assignment')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('position', models.CharField(choices=[('chief_editor', 'Editor-in-Chief'), ('administrator', 'Administrator'), ('web_developer', 'Web Developer'), ('editor', 'Section Editor'), ('author', 'Author'), ('guest', 'Guest Author'), ('photographer', 'Photographer'), ('graphic_designer', 'Graphic Designer')], max_length=50, default='author')),
                ('display_name', models.CharField(blank=True, max_length=50)),
                ('legacy_id', models.PositiveIntegerField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('reviewer', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('article', models.ForeignKey(to='mainsite.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('editor', models.ForeignKey(to='workflow.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='WArticle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.TextField()),
                ('article', models.OneToOneField(to='mainsite.Article')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(related_name='assignment_received', to='workflow.Profile'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(related_name='assignment', to='mainsite.Article', null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(related_name='assignment', to='mainsite.Photo', null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='sender',
            field=models.ForeignKey(related_name='assignment_created', to='workflow.Profile'),
        ),
    ]
