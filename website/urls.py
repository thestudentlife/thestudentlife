from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workflow/', include('workflow.urls')),
    url(r'^', include('mainsite.urls')),
)