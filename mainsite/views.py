from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section, Article, Profile

def home(request):
    return HttpResponse('This is the homepage');

def section(request, section_name):
    articles = Section.objects.get(name = section_name).articles.all();
    return render(request,'section.html',{"articles":articles});

def article(request, section_name, article_id, article_name='default'):
    article = Article.objects.get(pk=article_id);
    return HttpResponse('This is article ' + str(article_id) + ' with name ' + article_name + ' in section ' + section_name);


def person(request, person_id, person_name='ZQ'):
    person = Profile.objects.get(pk=person_id);
    if person.position=="author":
        articles = Article.objects.filter(author=person);
    if person.position=="photographer" or "graphic_designer":
        photos = Article.objects.filter(photographers=person);
    return HttpResponse('This is author ' + str(person_id) + ' with name ' + person_name);

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');