# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('article', models.OneToOneField(to='mainsite.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrontArticle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('article', models.OneToOneField(to='mainsite.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('maker_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='mainsite.Maker', serialize=False)),
            ],
            options={
            },
            bases=('mainsite.maker',),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('maker_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='mainsite.Maker', serialize=False)),
            ],
            options={
            },
            bases=('mainsite.maker',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='media/uploads/')),
                ('caption', models.TextField(max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('maker_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='mainsite.Maker', serialize=False)),
            ],
            options={
            },
            bases=('mainsite.maker',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='credit',
            field=models.ForeignKey(to='mainsite.Photographer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='mainsite.Author'),
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
            field=models.ForeignKey(to='mainsite.Section'),
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
