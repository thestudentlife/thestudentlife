from django.conf.urls import patterns, include, url
from mainsite import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^person/(?P<person_id>\d+)/(?P<person_name>.+)/$', views.person, name='person'),
    url(r'^person/(?P<person_id>\d+)/$', views.person, name='person'),
    url(r'^(?P<section_name>\w+)/$', views.section, name='section'),
    url(r'^(?P<section_name>\w+)/(?P<article_id>\d+)/(?P<article_name>.+)/$', views.article, name='article'),
    url(r'^(?P<section_name>\w+)/(?P<article_id>\d+)/$', views.article, name='article'),
    )
