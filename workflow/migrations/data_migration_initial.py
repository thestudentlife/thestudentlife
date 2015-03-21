# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group, User

from django.db import models, migrations
from mainsite.models import Issue, Section, Article, FrontArticle, Album
from workflow.models import Profile, Assignment

class Migration(migrations.Migration):
    def initial_data(apps, schema_editor):
        plastic = Group(name="plastic")
        plastic.save()

        bronze = Group(name="bronze")
        bronze.save()

        silver = Group(name="silver")
        silver.save()

        gold = Group(name="gold")
        gold.save()

        kent = User(username="kshikama")
        kent.set_password("tsl")
        kent.save()
        kent.groups.add(gold, silver, bronze, plastic)
        kent_profile = Profile(user=kent, position="author")
        kent_profile.save();

        zq = User(username="zxiong")
        zq.set_password("tsl")
        zq.save()
        zq.groups.add(gold, silver, bronze, plastic)
        zq_profile = Profile(user=zq, position="photographer")
        zq_profile.save();

        latina = User(username="vlatina")
        latina.set_password("tsl")
        latina.save()
        latina.groups.add(bronze, plastic)
        latina_profile = Profile(user=latina, position="author")
        latina_profile.save()

        issue = Issue(name="SP 2015 1")
        issue.save()

        news = Section(name="news")
        news.save();
        sports = Section(name="sports")
        sports.save();

        zq.profile.article_set.create(title="Latina configures git!",
                                      content="She got a new copy of our repository! Yeah~",
                                      section=news,
                                      issue=issue)
        article = Article.objects.all()[0]

        front = FrontArticle(article=article)
        front.save()

        assignment1 = Assignment(sender=zq_profile, receiver=kent_profile, title="Take a photo of Latina Vidolova",
                                 content="Don't let her know!", section=sports, type="photo")
        assignment1.save()

        album = Album(article=article)
        album.save()

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]