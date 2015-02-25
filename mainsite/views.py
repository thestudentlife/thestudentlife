from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Section,Article,Author,Photographer

def home(request):
    return HttpResponse('This is the homepage');

def section(request, section_name):
    articles = Section.objects.get(name = section_name).articles;
    return HttpResponse('This is a section ' + section_name);

def article(request, section_name, article_id, article_name='default'):
    article = Article.objects.get(pk=article_id);
    return HttpResponse('This is article ' + str(article_id) + ' with name ' + article_name + ' in section ' + section_name);

def author(request, author_id, author_name='ZQ'):
    author = Author.objects.get(pk=author_id);
    articles = Article.objects.filter(author=author);
    return HttpResponse('This is author ' + str(author_id) + ' with name ' + author_name);

def photographer(request, photographer_id, photographer_name='ZQ'):
    photographer = Photographer.objects.get(pk=photographer_id);
    photos = Article.objects.filter(credit=photographer);
    return HttpResponse('This is photographer ' + str(photographer_id) + ' with name ' + photographer_name);

def designer(request, designer_id, designer_name='ZQ'):
    designer = Designer.objects.get(pk=designer_id);
    return HttpResponse('This is designer ' + str(designer_id) + ' with name ' + designer_name);

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');