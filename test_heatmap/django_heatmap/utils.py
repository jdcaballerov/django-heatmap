from django.db import models
from django.conf import settings
from django.utils.importlib import import_module

from .exceptions import InvalidBackend

def collection_disabled():
	return getattr(settings, 'DJANGO_HEATMAP_DISABLED', False)

def get_backend():
	return getattr(settings, 'DJANGO_HEATMAP_BACKEND', 'django_heatmap.backends.db')

def import_backend():
	backend_string = get_backend()
	try:
		backend = import_module(backend_string)
	except Exception, e:
		raise InvalidBackend("Could not load '%s' as a backend: %s" % (backend_string, e))
	return backend

def save_click(post_data, **kwargs):
	if collection_disabled():
		return
	
	backend = import_backend()
	backend.save_event(post_data, **kwargs)

def generate_heatmap(res_x,res_y,height,width,url,**kwargs):
	backend = import_backend()
	return backend.gen_heatmap(res_x,res_y,height,width,url,**kwargs)

