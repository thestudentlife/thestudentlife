from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from workflow.article_views import ArticleCreateView, ArticleDetailView, article_edit, ArticleDeleteView
from workflow.issue_views import IssueCreateView, IssueEditView
from workflow.views import group_required
from workflow import views
from workflow import issue_views
from workflow import photo_views

urlpatterns = patterns('',
                       url(r'^$', views.whome, name='whome'),

                       # login/register
                       url(r'^register/$', views.register, name="register"),
                       url(r'^login/$', views.login, name="login"),
                       url(r'^logout/$', views.logout, name="logout"),
                       url(r'^settings/(?P<user_id>[0-9]+)/$',views.setting,name="setting"),
                       url(r'^manage/$',views.manage,name='manage'),
                       url(r'^manage/(?P<user_id>[0-9]+)/$',views.manage_one,name='manage_one'),

                       #front
                       url(r'^front/$', views.front, name="front"),
                       url(r'^pub/(?P<article_id>[0-9]+)/',views.publish,name="publish"),

                       #issues
                       url(r'^articles/issues/$', issue_views.issues, name="issues"),
                       url(r'^articles/issue/(?P<issue_id>[0-9]+)/$', issue_views.issue, name="issue"),
                       url(r'^articles/issue/latest/$', issue_views.latest_issue, name="latest_issue"),
                       url(r'^articles/issue/new/$', group_required('silver')(IssueCreateView.as_view()),
                           name="new_issue"),
                       url(r'^articles/issue/(?P<pk>[0-9]+)/edit/$', group_required('silver')(IssueEditView.as_view()),
                           name="edit_issue"),

                       #articles
                       url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<pk>[0-9]+)/$',
                           group_required('silver')(ArticleDetailView.as_view()), name='warticle'),
                       url(r'^articles/issue/(?P<issue_id>[0-9]+)/new/$', login_required(ArticleCreateView.as_view()),
                           name='new_article'),
                       url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<pk>[0-9]+)/edit/$',
                           article_edit, name='edit_article'),
                       url(r'^articles/issue/(?P<issue_id>[0-9]+)/(?P<pk>[0-9]+)/delete/$',
                           group_required('silver')(ArticleDeleteView.as_view()), name='delete_article'),
                       url(r'^articles/xml/(?P<article_id>\d+)', views.article_xml, name="article_xml"),
                       url(r'^articles/revision/(?P<pk>\d+)/$', views.revision, name="revision"),
                       url(r'^comment/(?P<article_id>\d+)/(?P<user_id>\d+)/$', views.comment,name="comment"),

                       url(r'^albums$', photo_views.albums,name='albums'),
                       url(r'^album/(?P<issue_id>\d+)$', photo_views.issue_albums, name="issue_albums"),
                       url(r'^album/(?P<issue_id>\d+)/(?P<album_id>\d+)/$', photo_views.view_album, name="view_album"),
                       url(r'^album/(?P<issue_id>\d+)/(?P<album_id>\d+)/edit/$', photo_views.edit_album, name="edit_album"),

                       #photos
                       url(r'^photos/$', photo_views.photos, name="photos"),
                       #    url(r'^photos/(?P<photo_id>[0-9]+)/$',views.photo,name="photo"),
                       #    url(r'^photos/new/',PhotoCreateView.as_view(),name="new_photo"),
                       #    url(r'^photos/(?P<photo_id>[0-9]+)/edit/',views.edit_photo,name="edit_photo"),
                       #    url(r'^photos/upload/', login_required(PhotoCreateView.as_view()), name="upload_photo"),

                       #assignments
                       url(r'^assignments/$', views.assignments, name="assignments"),
                       url(r'^assignments/(?P<assignment_id>[0-9]+)/$', views.assignment, name="assignment"),
                       url(r'^assignments/new/$', views.new_assignment, name="new_assignment"),
                       url(r'^assignments/(?P<assignment_id>[0-9]+)/edit/$', views.edit_assignment,
                           name="edit_assignment"),
                       url(r'^assignments/receiver/(?P<profile_id>[0-9]+)$', views.filter_by_receiver,
                           name="filter_by_receiver"),
                       url(r'^assignments/section/(?P<section_id>[0-9]+)$', views.filter_by_section,
                           name="filter_by_section"),
                       url(r'^assignments/type/(?P<type_name>[a-z]+)$', views.filter_by_type, name="filter_by_type"),
)