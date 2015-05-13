# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group, User

from django.db import models, migrations
from mainsite.models import Issue, Section, Article, FrontArticle, Album
from workflow.models import Profile, Assignment, WArticle

class Migration(migrations.Migration):

    def initial_data(apps, schema_editor):
        plastic, bronze, silver, gold = Migration.createGroups()
        kent, kent_profile, zq, zq_profile, latina, latina_profile = Migration.createProfiles(bronze, gold, plastic, silver)
        issue = Migration.createIssues()
        news, life_and_style, sports, opinions = Migration.createSections()
        Migration.createArticles(issue, kent, zq, news, sports, opinions)
        Migration.createFrontArticle()
        Migration.createAssignments(kent_profile, zq_profile, life_and_style, sports)

    @staticmethod
    def createGroups():
        plastic = Group(name="plastic")
        plastic.save()
        bronze = Group(name="bronze")
        bronze.save()
        silver = Group(name="silver")
        silver.save()
        gold = Group(name="gold")
        gold.save()
        return plastic, bronze, silver, gold

    @staticmethod
    def createProfiles(bronze, gold, plastic, silver):
        kent = User(username="kshikama")
        kent.set_password("tsl")
        kent.save()
        kent.groups.add(gold, silver, bronze, plastic)
        kent_profile = Profile(user=kent, position="author", display_name="kshikama")
        kent_profile.save();
        zq = User(username="zxiong")
        zq.set_password("tsl")
        zq.save()
        zq.groups.add(gold, silver, bronze, plastic)
        zq_profile = Profile(user=zq, position="author", display_name="zxiong")
        zq_profile.save();
        latina = User(username="vlatina")
        latina.set_password("tsl")
        latina.save()
        latina.groups.add(gold, silver, bronze, plastic)
        latina_profile = Profile(user=latina, position="photographer", display_name="vlatina")
        latina_profile.save()
        return kent, kent_profile, zq, zq_profile, latina, latina_profile

    @staticmethod
    def createIssues():
        issue = Issue(name="SP 2015 1")
        issue.save()
        issue2 = Issue(name="SP 2015 2")
        issue2.save()
        return issue

    @staticmethod
    def createSections():
        news = Section(name="News")
        news.save()
        life_and_style = Section(name="Life and Style")
        life_and_style.save()
        sports = Section(name="Sports")
        sports.save()
        opinions = Section(name="Opinions")
        opinions.save()
        return news, life_and_style, sports, opinions

    @staticmethod
    def createArticles(issue, kent, zq, news, sports, opinions):
        article1 = zq.profile.article_set.create(title="Latina configures git!",
                                      content="She got a new copy of our repository! Yeah~",
                                      section=news,
                                      issue=issue)
        album1 = Album(article=article1)
        album1.save()
        workflowArticle1 = WArticle(article=article1, status='')
        workflowArticle1.save()

        article2 = kent.profile.article_set.create(title="This article is related to sports",
                                        content="Nothing much",
                                        section=sports,
                                        issue=issue)
        album2 = Album(article=article2)
        album2.save()
        workflowArticle2 = WArticle(article=article2, status='')
        workflowArticle2.save()

        article3 = kent.profile.article_set.create(title="This article is related to opinion",
                                        content="I think this section is important",
                                        section=opinions,
                                        issue=issue)
        album3 = Album(article=article3)
        album3.save()
        workflowArticle3 = WArticle(article=article3, status='')
        workflowArticle3.save()

    @staticmethod
    def createFrontArticle():
        article = Article.objects.all()[0]
        front = FrontArticle(article=article)
        front.save()

    @staticmethod
    def createAssignments(kent_profile, zq_profile, life_and_style, sports):
        assignment1 = Assignment(sender=zq_profile, receiver=kent_profile, title="Take a photo of Latina Vidolova",
                                 content="Don't let her know!", section=sports, type="photo")
        assignment1.save()
        assignment2 = Assignment(sender=kent_profile, receiver=zq_profile, title="Migrate data from old database",
                                 content="Good luck", section=life_and_style, type="photo")
        assignment2.save()

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]