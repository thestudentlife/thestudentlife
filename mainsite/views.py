from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('This is the homepage');

def section(request, section_name):
    return HttpResponse('This is a section ' + section_name);

def article(request, section_name, article_id, article_name='default'):
    return HttpResponse('This is article ' + str(article_id) + ' with name ' + article_name + ' in section ' + section_name);

def author(request, author_id, author_name='ZQ'):
    return HttpResponse('This is author ' + str(author_id) + ' with name ' + author_name);

def photographer(request, photographer_id, photographer_name='ZQ'):
    return HttpResponse('This is photographer ' + str(photographer_id) + ' with name ' + photographer_name);

def designer(request, designer_id, designer_name='ZQ'):
    return HttpResponse('This is designer ' + str(designer_id) + ' with name ' + designer_name);

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');