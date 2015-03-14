from django.conf.urls import patterns, include, url
from workflow import views

urlpatterns = patterns('',
    url(r'^$',views.home,name='home'),

    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.login,name="login"),
    #issues
    url(r'^articles/issues/$',views.issues,name="issues"),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/$',views.issue,name="issue"),
    url(r'^articles/issue/new/$',views.new_issue,name="new_issue"),
    #articles
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/(?P<article_name>[^/]+)/$',
    	views.article,name='article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/$',
        views.article,name='article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/new/$',views.new_article,name='new_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/(?P<article_name>.+)/edit/$',
    	views.edit_article,name='edit_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/edit/$',
        views.edit_article,name='edit_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/(?P<article_name>.+)/delete/$',
    	views.delete_article,name='delete_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)/delete/$',
        views.delete_article,name='delete_article'),
    url(r'^articles/author/(?P<author_id>\d+)/$',views.article_by_author,name='article_by_author'),
    url(r'^articles/xml/(?P<article_id>\d+)',views.article_xml,name="article_xml"),
	#photos
	url(r'^photos/$',views.photos,name="photos"),
	url(r'^photos/(?P<photo_id>[0-9]+)/$',views.photo,name="photo"),
	url(r'^photos/new/',views.new_photo,name="new_photo"),
	url(r'^photos/(?P<photo_id>[0-9]+)/edit/',views.edit_photo,name="edit_photo"),
    #assignments
    url(r'^assignments/$',views.assignments,name="assignments"),
    url(r'^assignments/(?P<assignment_id>[0-9]+)/$',views.assignment,name="assignment"),
    url(r'^assignments/new/$',views.new_assignment,name="new_assignment"),
    url(r'^assignments/(?P<assignment_id>[0-9]+)/edit/$',views.edit_assignment,name="edit_assignment"),
    url(r'^assignments/receiver/(?P<profile_id>[0-9]+)$',views.filter_by_receiver,name="filter_by_receiver"),
    url(r'^assignments/section/(?P<section_name>[a-z]+)$',views.filter_by_section,name="filter_by_section"),
    url(r'^assignments/type/(?P<type_name>[a-z]+)$',views.filter_by_type,name="filter_by_type"),
)