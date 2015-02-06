from django.conf.urls import patterns, include, url
from workflow import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.home,name='home'),

    #issues
    url(r'^articles/issues/$',views.issues,name="issues"),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/$',views.issue,name="issue"),
    url(r'^articles/issue/new/$',views.new,name="new_issue"),
    #articles
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)(/?P<article_name>.+)?/$',
    	views.article,name='article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/new/$',views.new_article,name='new_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)(/?P<article_name>.+)?/edit/$',
    	views.edit_article,name='edit_article'),
    url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<article_id>[0-9]+)(/?P<article_name>.+)?/delete/$',
    	views.delete_article,name='delete_article'),
	#photos
	url(r'^photos/',views.photos,name="photos"),
	url(r'^photos/(?P<photo_id>[0-9]+)/',views.photo,name="photo"),
	url(r'^photos/new/',views.new_photo,name="new_photo"),
	url(r'^photos/(?P<photo_id>[0-9]+)/edit/',views.edit_photo,name="edit_photo"),
)