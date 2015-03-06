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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('assignment_ptr', models.OneToOneField(auto_created=True, to='workflow.Assignment', parent_link=True, primary_key=True, serialize=False)),
                ('article', models.ForeignKey(default=None, to='mainsite.Article')),
            ],
            options={
            },
            bases=('workflow.assignment',),
        ),
        migrations.CreateModel(
            name='Photo_assignment',
            fields=[
                ('assignment_ptr', models.OneToOneField(auto_created=True, to='workflow.Assignment', parent_link=True, primary_key=True, serialize=False)),
                ('photo', models.ForeignKey(default=None, to='mainsite.Photo')),
            ],
            options={
            },
            bases=('workflow.assignment',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('position', models.CharField(max_length=50, default='Editor', choices=[('chief_editor', 'Chief Editor'), ('copy_editor', 'Copy Editor'), ('photographer', 'Photographer'), ('author', 'Author'), ('graphic_designer', 'Graphic Designer')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('article', models.ForeignKey(to='mainsite.Article')),
                ('editor', models.ForeignKey(to='workflow.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
            field=models.ForeignKey(related_name='receiver', default=None, to='workflow.Profile'),
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
            field=models.ForeignKey(related_name='sender', to='workflow.Profile'),
            preserve_default=True,
        ),
    ]
