from django.contrib.auth.models import Permission, User, Group, ContentType
from mainsite.models import Issue, Article, Section
from workflow.models import Profile
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

zq = User(username="zxiong")
zq.set_password("tsl")
zq.save()
zq.groups.add(gold, silver, bronze, plastic)
zq_profile = Profile(user=zq,position="web_developer")
zq_profile.save();

latina = User(username="vlatina")
latina.set_password("tsl")
latina.save()
latina.groups.add(gold, silver, bronze, plastic)

issue = Issue(name="SP 2015 1")
issue.save()

news = Section(name="news")
news.save();
sports = Section(name="sports")
sports.save();

article = Article(title="Latina configures git!",
                   content="She got a new copy of our repository! Yeah~",
                   section=news,
                   issue=issue)
article.authors.add(zq_profile)
article.save();
print(article)