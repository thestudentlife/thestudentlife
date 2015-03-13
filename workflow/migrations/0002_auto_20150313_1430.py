# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20150313_1430'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentForm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='article_assignment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='article_assignment',
            name='assignment_ptr',
        ),
        migrations.DeleteModel(
            name='Article_Assignment',
        ),
        migrations.RemoveField(
            model_name='photo_assignment',
            name='assignment_ptr',
        ),
        migrations.RemoveField(
            model_name='photo_assignment',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Photo_assignment',
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_article',
            field=models.ForeignKey(null=True, related_name='assignment', to='mainsite.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='response_photo',
            field=models.ForeignKey(null=True, related_name='assignment', to='mainsite.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='type',
            field=models.CharField(choices=[('photo_assignment', 'Photo Assignment'), ('article_assignment', 'Article Assignment')], max_length=50, default='photo_assignment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('chief_editor', 'Chief Editor'), ('copy_editor', 'Copy Editor'), ('photographer', 'Photographer'), ('author', 'Author'), ('graphic_designer', 'Graphic Designer')], max_length=50, default='Editor'),
            preserve_default=True,
        ),
    ]
