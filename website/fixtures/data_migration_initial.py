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
        Migration.createArticles(issue, kent, zq, news, life_and_style, sports, opinions)
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
        return issue2

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
    def createArticles(issue, kent, zq, news, life_and_style, sports, opinions):
        article1 = zq.profile.article_set.create(title="Latina configures git!",
                                      content="<p>She got a new copy of our repository! Yeah!</p>",
                                      section=news,
                                      issue=issue)
        album1 = Album(article=article1)
        album1.save()
        workflowArticle1 = WArticle(article=article1, status='')
        workflowArticle1.save()

        article2 = kent.profile.article_set.create(title="Poets Sink Sagehens 7-6 in SCIAC Championship Game",
                                        content="<p>The Pomona-Pitzer women's water polo team (19-10, 10-1 SCIAC) took to Haldeman Pool for the 2015 SCIAC Championships April 24-26 in hopes of winning its fourth straight SCIAC title.</p><p>Despite some dominant performances in the first two days of the tournament, the Sagehens were defeated 7-6 by Whittier College (21-14, 9-2 SCIAC) in the championship game after being heavily outscored in the opening half. The loss to Whittier snapped the Sagehens' 10-game SCIAC win streak and ended their perfect SCIAC season. P-P's record of 10-1 in SCIAC, however, still technically gives them the same amount of points in the SCIAC scoring system, so P-P will share the league title with Whittier for the 2015 season.</p>",
                                        section=sports,
                                        issue=issue)
        album2 = Album(article=article2)
        album2.save()
        workflowArticle2 = WArticle(article=article2, status='')
        workflowArticle2.save()

        article3 = kent.profile.article_set.create(title="This Article is Related to Opinion",
                                        content="<p>I think this article is important</p>",
                                        section=opinions,
                                        issue=issue)
        album3 = Album(article=article3)
        album3.save()
        workflowArticle3 = WArticle(article=article3, status='')
        workflowArticle3.save()

        article4 = kent.profile.article_set.create(title="Reza Aslan on Religion and the Rise of Secularism at American Colleges",
                                        content="<p>Reza Aslan is a scholar of religious studies and a professor of creative writing at the University of California, Riverside. His publications include the international bestsellers No god but God: The Origins, Evolution, and Future of Islam and Zealot: The Life and Times of Jesus of Nazareth. The latter is a historical account and interpretation of the life of Jesus. Aslan has been a critic of the “New Atheist” movement and has openly denounced what he terms the “anti-theism” advocated by public figures like Sam Harris, Richard Dawkins and Bill Maher.</p>",
                                        section=life_and_style,
                                        issue=issue)
        album4 = Album(article=article4)
        album4.save()
        workflowArticle4 = WArticle(article=article4, status='')
        workflowArticle4.save()

        article4 = kent.profile.article_set.create(title="Senior Art Exhibitions Showcase Final Thesis Works of Art Majors",
                                        content="<p>Things You Can't Explain, the annual exhibition of final thesis works produced by graduating studio art majors from Harvey Mudd College and Scripps College, will take place beginning May 1 in Scripps' Ruth Chandler Williamson Gallery. This year's show will feature the work of Lily Alan SC '15, Teagan Blain-Rozgay SC '15, Mabelle Bong SC '15, Susanna Ferrell SC '15, Leah Hughes SC '15, Haley Ross SC '15, Seana Rothman SC '15 and Allison Schubauer HM '15. According to Alan, the show has no unifying theme and was difficult to name as a consequence. The artists had different visions for their pieces and worked with a variety of materials.</p>",
                                        section=life_and_style,
                                        issue=issue)
        album4 = Album(article=article4)
        album4.save()
        workflowArticle4 = WArticle(article=article4, status='')
        workflowArticle4.save()


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