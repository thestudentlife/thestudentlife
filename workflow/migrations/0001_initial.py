# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article_Assignment',
            fields=[
                ('assignment_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='workflow.Assignment', serialize=False)),
                ('article', models.ForeignKey(default=None, to='mainsite.Article')),
            ],
            options={
            },
            bases=('workflow.assignment',),
        ),
        migrations.CreateModel(
            name='Photo_assignment',
            fields=[
                ('assignment_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='workflow.Assignment', serialize=False)),
                ('photo', models.ForeignKey(default=None, to='mainsite.Photo')),
            ],
            options={
            },
            bases=('workflow.assignment',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('position', models.CharField(max_length=50, choices=[('ChiefEditor', 'Chief Editor'), ('CopyEditor', 'Copy Editor')], default='Editor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviewer', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('article', models.ForeignKey(to='mainsite.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('editor', models.ForeignKey(to='mainsite.Editor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WArticle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField()),
                ('article', models.OneToOneField(to='mainsite.Article')),
                ('locker', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
            field=models.ForeignKey(default=None, to='mainsite.Maker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(to='mainsite.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='sender',
            field=models.ForeignKey(to='mainsite.Editor'),
            preserve_default=True,
        ),
    ]
