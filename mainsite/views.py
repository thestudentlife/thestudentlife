from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section, Article, Profile,FrontArticle

def home(request):
    sections = Section.objects.all()
    articles = {}
    for section in sections:
        articles[section.name]=[]
    front_articles = FrontArticle.objects.all()
    for front_article in front_articles:
        articles[front_article.article.section.name].append(front_article.article)
    return render(request, 'index.html',{'sections':sections,'articles':articles})

def section(request, section_name):
    sections = Section.objects.all()
    sec = 0
    for section in sections:
        if section.slug() == section_name:
            sec = section;
    articles = sec.articles.order_by('-published_date')[:10];
    return render(request, 'section.html', {"articles": articles});

def article(request, section_name, article_id, article_name='default'):
    article = Article.objects.get(pk=article_id);
    return render(request, 'article.html', {"article": article})

def person(request, person_id, person_name='ZQ'):
    person = Profile.objects.get(pk=person_id);
    if person.position == "author":
        articles = person.article_set.all();
        return render(request, 'author.html', {"articles": articles});
    if person.position == "photographer" or person.position == "graphic_designer":
        photographs = person.photo_set.all();
        return render(request, 'photographer.html', {"photographs": photographs});

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');