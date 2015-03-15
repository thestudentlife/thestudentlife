# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(default=b'photo_assignment', max_length=50, choices=[(b'photo_assignment', b'Photo Assignment'), (b'article_assignment', b'Article Assignment')])),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50, default='photo_assignment', choices=[('photo_assignment', 'Photo Assignment'), ('article_assignment', 'Article Assignment')])),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='AssignmentForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(default=b'Editor', max_length=50, choices=[(b'chief_editor', b'Chief Editor'), (b'copy_editor', b'Copy Editor'), (b'photographer', b'Photographer'), (b'author', b'Author'), (b'graphic_designer', b'Graphic Designer'), (b'web_developer', b'Web Developer')])),
=======
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('position', models.CharField(max_length=50, default='Editor', choices=[('chief_editor', 'Chief Editor'), ('copy_editor', 'Copy Editor'), ('photographer', 'Photographer'), ('author', 'Author'), ('graphic_designer', 'Graphic Designer'), ('web_developer', 'Web Developer')])),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
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
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
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
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField()),
                ('article', models.OneToOneField(to='mainsite.Article')),
                ('locker', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assignment',
            name='receiver',
<<<<<<< HEAD
            field=models.ForeignKey(related_name='assignment_received', default=None, to='workflow.Profile'),
=======
            field=models.ForeignKey(related_name='assignment_received', to='workflow.Profile', null=True),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(related_name='assignment', to='mainsite.Article', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(related_name='assignment', to='mainsite.Photo', null=True),
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
            field=models.ForeignKey(related_name='assignment_created', to='workflow.Profile'),
            preserve_default=True,
        ),
    ]
