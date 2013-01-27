from django.conf.urls import patterns, url
from django.views.generic import ListView

from .models import Page
from .views import save_click_event,show_click_events,test_events

from djcelery.views import is_task_successful

urlpatterns = patterns('',
	url(r'^$',ListView.as_view(queryset=Page.objects.all(),context_object_name='page_list',template_name='page_list.html'),name='index'),
    url(r'^show_clicks/(?P<res_x>\d+)/(?P<res_y>\d+)/(?P<height>\d+)/(?P<width>\d+)/(?P<url>.+)/$', show_click_events, name='show_click_events'), 
    url(r'^get_clicks/(?P<res_x>\d+)/(?P<res_y>\d+)/(?P<height>\d+)/(?P<width>\d+)/(?P<url>.+)/$', show_click_events, name='get_click_events'), 
	url(r'^save_click_event/$', save_click_event, name='save_click_event'), 

	url(r'^test_events/$',test_events,name='test_events'),    
)

urlpatterns += patterns('',
    url(r'(?P<task_id>[\w\d\-\.]+)/done/?$', is_task_successful,
        name='celery-is_task_successful'),
    )
