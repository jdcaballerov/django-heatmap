from django.conf import settings
from django.conf.urls import patterns, include, url

from .views import test_events

if settings.DEBUG:
	from django.conf.urls.defaults import *
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_heatmap.views.home', name='home'),
    # url(r'^test_heatmap/', include('test_heatmap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^test_events/$',test_events,name='test_events'), 
    url(r'^heatmap/', include('django_heatmap.urls')),
	
)

if settings.DEBUG:
	urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	'document_root': settings.MEDIA_ROOT,}),)
	urlpatterns += staticfiles_urlpatterns()
