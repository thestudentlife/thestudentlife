from django.conf.urls import patterns, include, url
from mainsite import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^author/(?P<author_id>\d+)/(?P<author_name>.+)/$', views.author, name='author'),
    url(r'^author/(?P<author_id>\d+)/$', views.author, name='author'),
    url(r'^photographer/(?P<photographer_id>\d+)/(?P<photographer_name>.+)/$', views.photographer, name='photographer'),
    url(r'^photographer/(?P<photographer_id>\d+)/$', views.photographer, name='photographer'),
    url(r'^designer/(?P<designer_id>\d+)/(?P<designer_name>.+)/$', views.designer, name='designer'),
    url(r'^designer/(?P<designer_id>\d+)/$', views.designer, name='designer'),
    url(r'^(?P<section_name>\w+)/$', views.section, name='section'),
    url(r'^(?P<section_name>\w+)/(?P<article_id>\d+)/(?P<article_name>.+)/$', views.article, name='article'),
    url(r'^(?P<section_name>\w+)/(?P<article_id>\d+)/$', views.article, name='article'),
    )
