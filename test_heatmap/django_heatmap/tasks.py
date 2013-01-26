import StringIO
import base64

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

from .models import Page, ClickItem

import heatmap

try:
    from celery.task import task
except ImportError:
    from celery.decorators import task

@task
def db_save_click_task(post_data, **kwargs):
	
	res_x = int(post_data['resx'])
	res_y = int(post_data['resy'])
	width = int(post_data['width'])
	height = int(post_data['height'])

	#print post_data['url'],res_x,res_y,int(post_data['x']),int(post_data['y'])
	try:
		page,created = Page.objects.get_or_create(url=post_data['url'],res_x=res_x,res_y=res_y,width=width,height=height)
		click = ClickItem(page=page,x=int(post_data['x']),y=int(post_data['y']))
		click.save()
	except Exception, e:
		print e
	
	return

#TODO Only generate if some parameters change - cache
@task
def db_generate_heatmap(res_x,res_y,height,width,url):
	pts = []
	page = Page.objects.get(url=url,res_x=int(res_x),res_y=int(res_y),width=int(width),height=int(height))
	clicks = ClickItem.objects.all().filter(page=page)
	for item in clicks:
		pts.append((item.x,page.height-item.y))
	hm = heatmap.Heatmap()
	img = hm.heatmap(pts,area=((0,0),(page.width,page.height)),size=(page.width,page.height),dotsize=50)
	#save file to media
	url_id = base64.urlsafe_b64encode(page.url)
	output = StringIO.StringIO()	
	img.save(output, 'PNG')
	f1 = ContentFile(output.getvalue())
	default_storage.save('%s.png' % (url_id),f1)
	output.close()
	

	#img.save('%s@%dx%d.png' % (url,int(res_x),int(res_y)))
	#img.save('cas.png')
	#response = HttpResponse(mimetype="image/png")
	#img.save(response,'PNG')
	return
	#return response
