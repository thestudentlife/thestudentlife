from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from django.views.decorators.clickjacking import xframe_options_exempt
from mainsite.models import Section, Article, Profile, FrontArticle, CarouselArticle, Copy, StaticPage
import json
from datetime import datetime, timedelta


def home(request):
    features = CarouselArticle.objects.all()
    fronts = list(map(lambda x: x.article, FrontArticle.objects.order_by("article__section__priority").all()))
    comics = Article.objects.filter(title__startswith="Weekly Comic").order_by('-created_date')
    comic_url = None
    if len(comics) > 0:
        k = 0
        comic = comics[k]
        while len(comic.album.photo_set.all()) == 0 and k<len(comics):
            comic = comics[k]
            k+=1
        if len(comic.album.photo_set.all()) > 0:
            comic_url = comic.album.photo_set.all()[0].image.url
    return render(request, 'index.html', {'features': features, 'fronts': fronts, 'recents': get_recent(5),
                                          'populars': get_popular(5), 'comic_url': comic_url})

def page(request, name):
    page = StaticPage.objects.get(name=name)
    return render(request, 'static.html', {'page': page})

def section(request, section_slug):
    sections = Section.objects.all().order_by('priority')
    this_section = 0
    for section in sections:
        if section.slug() == section_slug:
            this_section = section
    if this_section == 0:
        return error404(request)
    if request.is_ajax():
        count = int(request.GET['count'])
        articles = this_section.articles.order_by('-published_date')[count:count + 10]
        articles_in_json = []
        for article in articles:
            if article.published:
                articles_in_json.append(article_ajax_object(article))
        return HttpResponse(json.dumps(articles_in_json), content_type='application/json')
    articles = this_section.articles.filter(published=True).order_by('-published_date')[:10]
    return render(request, 'section.html', {"section": this_section, "articles": articles, 'recents': get_recent(5), 'populars': get_popular(5)})

@xframe_options_exempt
def article(request, section_name, article_id, article_name='default'):
    article = get_object_or_404(Article,pk=article_id)
    article.click()
    article.save()
    if not article.published:
        return error404(request)
    return render(request, 'article.html', {"article": article, 'recents': get_recent(5), 'populars': get_popular(5)})

def legacy_article(request,legacy_id):
    a = Article.objects.get(legacy_id=legacy_id)
    return article(request,'articles',article_id=a.id)

def error404(request):
    return render(request, '404.html')

def person(request, person_id, person_name='ZQ'):
    person = get_object_or_404(Profile, pk=person_id)
    if person.position == "author" or len(person.article_set.all().filter(published=True)) > 0:
        articles = person.article_set.all().filter(published=True)
        recents = person.article_set.all().filter(published=True).order_by('-published_date')[:5]
        populars = person.article_set.all().filter(published=True).order_by('-clicks')[:5]
        return render(request, 'author.html',
                      {"person": person, "articles": articles, 'recents': recents, 'populars': populars})
    elif person.position == "photographer" or person.position == "graphic_designer":
        images = person.photo_set.all()
        return render(request, 'photographer.html',
                      {"person": person, "images": images, 'recents': get_recent(5), 'populars': get_popular(5)})
    else:
        return HttpResponse('His/Her profile is not public.')


def google_search(request):
    query = request.GET.get('q')
    return render(request, "search_result.html", {'query':query})

def other(request, info):
    template = "other/" + info + ".html";
    return render(request, "other/about.html", {'info': template})

def archives(request):
    copies = Copy.objects.all()
    return render(request, 'other/archives.html', {'copies': copies})  # Create json objects for an article

def article_ajax_object(article):
    fmt = '%b. %d, %Y, %I:%M %p'
    obj = dict()
    obj['url'] = article.get_absolute_url()
    obj['title'] = article.title
    obj['section'] = {'name': article.section.name,
                      'url': article.section.get_absolute_url()}
    obj['published_date'] = article.published_date.strftime(fmt)
    obj['content'] = article.content[0:200] + '...'
    obj['disqus_id'] = article.disqus_id()
    obj['authors'] = []
    for author in article.authors.all():
        obj['authors'].append({'name': author.display_name, 'url': author.get_absolute_url()})
    return obj

def get_recent(n):
    last_month = datetime.today() - timedelta(days=30)
    return Article.objects.all().filter(published=True, published_date__gte=last_month).order_by('-published_date')[:n]

def get_popular(n):
    last_month = datetime.today() - timedelta(days=30)
    return Article.objects.all().filter(published=True, published_date__gte=last_month).order_by('-clicks')[:n]

from haystack.inputs import AutoQuery
from django.db.models import Q
def search_query(request):
    query = request.GET['search']
    if request.is_ajax():
        count = int(request.GET['count'])
        articles = SearchQuerySet().filter(Q(authors=AutoQuery(query)) | Q(content=query))[count:count+10]
        articles_in_json = []
        for article in articles:
            articles_in_json.append(article_ajax_object(article.object))
        return HttpResponse(json.dumps(articles_in_json), content_type='application/json')
    query_set = SearchQuerySet().filter(Q(authors=AutoQuery(query)) | Q(content=query))[:10]
    return render(request, "search/search.html", {"word": query, "qs": query_set, 'recents': get_recent(5), 'populars': get_popular(5)})
