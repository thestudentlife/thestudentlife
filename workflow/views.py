from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
# Create your views here.

#issues
def issues(request):
	return HttpResponse('These are the issues.')

def issue(request,issue_id):
	return HttpResponse('This is issue '+str(issue_id))

def new_issue(request):
	return HttpResponse('Create a new issue')

#articles
def article(request,issue_id,article_id):
	return HttpResponse('This is issue '+issue_id+" and article "+str(article_id))

def new_article(request):
	return HttpResponse('Create a new article')

def edit_article(request,issue_id,article_id):
	return HttpResponse('You are going to edit article '+str(article_id))

def delete_article(request,issue_id,article_id):
	return HttpResponse('You are going to delete article '+str(article_id))

#photos
def photos(request):
	return HttpResponse('These are the photos.')

def photo(request,photo_id):
	return HttpResponse('This is photo '+str(photo_id))

def new_photo(request):
	return HttpResponse('Create a new photo') 

def edit_photo(request,photo_id):
	return HttpResponse('You are going to edit article '+str(photo_id))

def home(request):
	return HttpResponse('This should be the latest issue.')






