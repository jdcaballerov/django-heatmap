import base64

from django.core import serializers
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from .utils import save_click,generate_heatmap

#test view includes
from django.shortcuts import render_to_response
from django.template import RequestContext


def show_click_events(request,res_x,res_y,height,width,url):
	task = generate_heatmap(res_x,res_y,height,width,url)
	url_img = base64.urlsafe_b64encode(url)
	return render_to_response('heatmap_overlay.html', {'url':url,'task': task,'url_img':url_img+'.png'},context_instance = RequestContext(request))
 
@csrf_exempt
def save_click_event(request):
	if request.is_ajax() and request.method == 'POST':
		message = "This is an XHR POST request"
        # Here we can access the POST data
		datos_post = request.POST
		#print datos_post
		#print datos_post
		save_click(datos_post)
	else:
		message = "No XHR or GET"   
 
	response = HttpResponse(message)
	return response

# TEST VIEW Includes JS code to send clicks to the server 
def test_events(request):
	return render_to_response("test.html", dict(user=request.user),context_instance = RequestContext(request))
	

	

