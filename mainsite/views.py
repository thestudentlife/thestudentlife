from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from mainsite.models import Section, Article, Profile, FrontArticle, CarouselArticle, Copy
import json


def home(request):
    sections = Section.objects.all()
    features = CarouselArticle.objects.all()
    fronts = FrontArticle.objects.all()
    return render(request, 'index.html',
                  {'sections': sections, 'features': features, 'fronts': fronts, 'recents': get_recent(5),
                   'populars': get_popular(5)})

def section(request, section_slug):
    sections = Section.objects.all()
    this_section = 0
    for section in sections:
        if section.slug() == section_slug:
            this_section = section;
    if this_section == 0:
        return error404(request);
    if request.is_ajax():
        count = int(request.GET['count'])
        articles = this_section.articles.order_by('-published_date')[count:count + 10]
        articles_in_json = []
        for article in articles:
            if article.published:
                articles_in_json.append(article_ajax_object(article))
        return HttpResponse(json.dumps(articles_in_json), content_type='application/json')
    articles = this_section.articles.filter(published=True).order_by('-published_date')[:10]
    return render(request, 'section.html', {"section": this_section, "sections": sections, "articles": articles,
                                            'recents': get_recent(5), 'populars': get_popular(5)});

def article(request, section_name, article_id, article_name='default'):
    sections = Section.objects.all()
    article = get_object_or_404(Article,pk=article_id)
    article.click()
    article.save()
    return render(request, 'article.html', {"sections": sections, "article": article, 'recents': get_recent(5),
                                            'populars': get_popular(5)})

def legacy_article(request,legacy_id):
    return article(request,'articles',article_id=legacy_id)

def error404(request):
    return render(request,'404.html')

def person(request, person_id, person_name='ZQ'):
    sections = Section.objects.all()
    person = get_object_or_404(Profile,pk=person_id)
    if person.position == "author" or len(person.article_set.all().filter(published=True)) > 0:
        articles = person.article_set.all().filter(published=True)
        recents = person.article_set.all().filter(published=True).order_by('-published_date')[:5]
        populars = person.article_set.all().filter(published=True).order_by('-clicks')[:5]
        return render(request, 'author.html',
                      {"person": person, "sections": sections, "articles": articles, 'recents': recents, 'populars': populars})
    elif person.position == "photographer" or person.position == "graphic_designer":
        images = person.photo_set.all()
        return render(request, 'photographer.html',
                      {"person": person, "sections": sections, "images": images, 'recents': get_recent(5), 'populars': get_popular(5)})
    else:
        return HttpResponse('His/Her profile is not public.')

def other(request, info):
    sections = Section.objects.all()
    template = "other/" + info + ".html";
    return render(request, "other/about.html", {"sections": sections, 'info': template})

def archives(request):
    sections = Section.objects.all()
    copies = Copy.objects.all()
    return render(request, 'other/archives.html', {"sections": sections, 'copies': copies})  # Create json objects for an article

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
        obj['authors'].append({'name': author.display_name,
                               'url': author.get_absolute_url()})
    return obj

def get_recent(n):
    return Article.objects.all().filter(published=True).order_by('-published_date')[:n]

def get_popular(n):
    return Article.objects.all().filter(published=True).order_by('-clicks')[:n]

def search_query(request):
    sections = Section.objects.all()
    query = request.GET['search']
    if request.is_ajax():
        count = int(request.GET['count'])
        articles = SearchQuerySet().filter(content=query)[count:count+10]
        articles_in_json = []
        for article in articles:
            articles_in_json.append(article_ajax_object(article.object))
        return HttpResponse(json.dumps(articles_in_json), content_type='application/json')
    query_set = SearchQuerySet().filter(content=query)[:10]
    return render(request, "search/search.html", {"sections": sections, "word": query, "qs": query_set, 'recents': get_recent(5), 'populars': get_popular(5)})

