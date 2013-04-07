from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
     url(r'^$', 'home.views.homepage'),
     url(r'^home/', 'home.views.homepage'),

)
