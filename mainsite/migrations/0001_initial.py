# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarouselArticle',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrontArticle',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to=b'photo/')),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='photo/')),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('caption', models.TextField(max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
>>>>>>> e49c23bf1566fb26e60209ed719bd2c9da909757
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
