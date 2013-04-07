from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import os

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'home.views.homepage'),
     url(r'^home/', 'home.views.homepage'),
)

urlpatterns += patterns('',
    (r'^static/(?<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
)
