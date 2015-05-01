from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section, Article, Profile,FrontArticle
import json

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
    if(request.is_ajax()):
        count = request.GET['count']
        articles = sec.articles.order_by('-published_date')[count:count+10]
        articles_in_json = []
        for article in articles:
            articles_in_json.append(article_ajax_object(article))
        return HttpResponse(json.dumps(articles_in_json),content_type='application/json')
    articles = sec.articles.order_by('-published_date')[:10]
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

# Create json objects for an article
def article_ajax_object(article):
    obj = dict()
    obj['url'] = article.get_absolute_url()
    obj['title'] = article.title
    obj['section'] = {'name':article.section.name,
                      'url':article.section.get_absolute_url()}
    obj['authors']=[]
    for author in article.authors.all():
        obj['authors'].append({'name':author.display_name,
                              'url':author.get_absolute_url()})
    return obj
