from django.conf.urls import patterns, include, url
from mainsite import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^other/(?P<info>\w+)/$', views.other, name='other'),
                       url(r'^archives/$', views.archives, name='archives'),
                       url(r'^person/(?P<person_id>\d+)/$', views.person, name='person'),
                       url(r'^(?P<section_slug>[^/]+)/$', views.section, name='section'),
                       url(r'^(?P<section_name>[^/]+)/(?P<article_id>\d+)/(?P<article_name>.+)/$', views.article,
                           name='article'),
                       url(r'^(?P<section_name>[^/]+)/(?P<article_id>\d+)/$', views.article, name='article'),
)
