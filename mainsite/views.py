from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section, Article, Profile,FrontArticle, CarouselArticle
import json

def home(request):
    sections = Section.objects.all()
    features = CarouselArticle.objects.all()
    fronts = FrontArticle.objects.all()
    recents = Article.objects.all().order_by('-published_date')[:5]
    return render(request, 'index.html', {'sections':sections,'features':features,'fronts':fronts,'recents':recents})

def section(request, section_slug):
    sections = Section.objects.all()
    this_section = 0
    for section in sections:
        if section.slug() == section_slug:
            this_section = section;
    if request.is_ajax():
        count = int(request.GET['count'])
        articles = this_section.articles.order_by('-published_date')[count:count+10]
        articles_in_json = []
        for article in articles:
            if article.published:
                articles_in_json.append(article_ajax_object(article))
        return HttpResponse(json.dumps(articles_in_json),content_type='application/json')
    articles = this_section.articles.filter(published=True).order_by('-published_date')[:10]
    recents = this_section.articles.order_by('-published_date')[:5]
    return render(request, 'section.html', {"section": this_section, "sections": sections, "articles": articles, 'recents': recents});

def article(request, section_name, article_id, article_name='default'):
    sections = Section.objects.all()
    article = Article.objects.get(pk=article_id)
    recents = Article.objects.all().order_by('-published_date')[:5]
    return render(request, 'article.html', {"sections": sections, "article": article, 'recents': recents})

def person(request, person_id, person_name='ZQ'):
    sections = Section.objects.all()
    person = Profile.objects.get(pk=person_id)
    if person.position == "author":
        articles = person.article_set.all().filter(published=True)
        recents = person.article_set.all().order_by('-published_date')[:5]
        return render(request, 'author.html', {"sections": sections, "articles": articles, 'recents': recents})
    if person.position == "photographer" or person.position == "graphic_designer":
        photographs = person.photo_set.all()
        return render(request, 'photographer.html', {"sections": sections, "photographs": photographs})
    return HttpResponse('His/Her profile is not public.')

def staff(request):
    return HttpResponse('Staff page')

def subscriptions(request):
    return HttpResponse('Subscriptions page')

def about(request):
    return HttpResponse('About page')

def archives(request):
    return HttpResponse('Archives page')

# Create json objects for an article
def article_ajax_object(article):
    fmt = '%Y-%m-%d %H:%M'
    obj = dict()
    obj['url'] = article.get_absolute_url()
    obj['title'] = article.title
    obj['section'] = {'name':article.section.name,
                      'url':article.section.get_absolute_url()}
    obj['published_date'] = article.published_date.strftime(fmt)
    obj['content'] = article.content[0:100]+'...'
    obj['authors']=[]
    for author in article.authors.all():
        obj['authors'].append({'name':author.display_name,
                              'url':author.get_absolute_url()})
    return obj
