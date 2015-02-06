from django.conf.urls import patterns, include, url
from mainsite import views

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^(?P<section>\w+)/$', 'views.section', name='section'),
    url(r'^(?P<section>\w+)/(?P<article_id>\d+)/(?P<article>.+)/$', 'views.article', name='article'),
    url(r'^author/(?P<author_id>\d+)/(?P<author_name>[\w]+(-[\w]+)/$', 'views.author', name='author'),
    url(r'^photographer/(?P<photographer_id>\d+)/(?P<photographer_name>[\w]+(-[\w]+)/$', 'views.photographer', name='photographer'),
    url(r'^staff$', 'views.staff', name='staff'),
    url(r'^subscriptions', 'views.subscriptions', name='subscriptions'),
    url(r'^about', 'views.about', name='about'),
    url(r'^archives', 'views.archives', name='archives'),
)
