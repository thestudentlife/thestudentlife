import django
django.setup()
from django.contrib.auth.models import Permission, User, Group, ContentType
from mainsite.models import Issue,Section, Article
from workflow.models import Profile

kent = Group.objects.all()[3].user_set.all()[0]
print("username for kent: " + kent.username)
print("password for kent: " + kent.password)

ziqi = Group.objects.all()[3].user_set.all()[1]
print("username for ziqi: " + ziqi.username)
print("password for ziqi: " + ziqi.password)

latina = Group.objects.all()[3].user_set.all()[2]
print("username for latina: " + latina.username)
print("password for latina: " + latina.password)

issue = Issue.objects.all()[0]
print("issue is "+issue.name)

profiles = Profile.objects.all()
for profile in profiles:
    print("profile user: "+profile.user.username)
    print("profile position: "+profile.position)

sections = Section.objects.all()
for section in sections:
    print("section name: "+section.name)

articles = Article.objects.all()
for article in articles:
    print("article title: "+article.title)
    print("article author: "+article.author.user.username)
    print("article content: "+article.content)

print("End test")