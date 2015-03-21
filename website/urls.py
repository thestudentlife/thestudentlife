from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^search/', include('haystack.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^workflow/', include('workflow.urls')),
                       url(r'^', include('mainsite.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
    )