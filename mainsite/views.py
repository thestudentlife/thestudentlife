from django.shortcuts import render
from django.http import HttpResponse
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
    article = Article.objects.get(pk=article_id)
    article.click()
    article.save()
    return render(request, 'article.html', {"sections": sections, "article": article, 'recents': get_recent(5),
                                            'populars': get_popular(5)})

def person(request, person_id, person_name='ZQ'):
    sections = Section.objects.all()
    person = Profile.objects.get(pk=person_id)
    if person.position == "author":
        articles = person.article_set.all().filter(published=True)
        recents = person.article_set.all().filter(published=True).order_by('-published_date')[:5]
        populars = person.article_set.all().filter(published=True).order_by('-clicks')[:5]
        return render(request, 'author.html',
                      {"person": person, "sections": sections, "articles": articles, 'recents': recents, 'populars': populars})
    if person.position == "photographer" or person.position == "graphic_designer":
        images = person.photo_set.all()
        return render(request, 'photographer.html',
                      {"person": person, "sections": sections, "images": images, 'recents': get_recent(5), 'populars': get_popular(5)})
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
    obj['content'] = article.content[0:100] + '...'
    obj['authors'] = []
    for author in article.authors.all():
        obj['authors'].append({'name': author.display_name,
                               'url': author.get_absolute_url()})
    return obj

def get_recent(n):
    return Article.objects.all().filter(published=True).order_by('-published_date')[:n]

def get_popular(n):
    return Article.objects.all().filter(published=True).order_by('-clicks')[:n]