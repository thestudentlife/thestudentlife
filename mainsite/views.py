from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('This is the homepage');

def section(request):
    return HttpResponse('This is a section page');

def article(request, article_id):
    return HttpResponse('This is article ' + str(article_id));

def author(request, author_id):
    return HttpResponse('This is author ' + str(author_id));

def photographer(request, photographer_id):
    return HttpResponse('This is photographer ' + str(photographer_id));

def staff(request):
    return HttpResponse('Staff page');

def subscriptions(request):
    return HttpResponse('Subscriptions page');

def about(request):
    return HttpResponse('About page');

def archives(request):
    return HttpResponse('Archives page');