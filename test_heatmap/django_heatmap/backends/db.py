from ..tasks import db_save_click_task,db_generate_heatmap

def save_event(post_data, **kwargs):
	""" Fire a celery task to record the click in the database """	
	db_save_click_task.delay(post_data, **kwargs)

def gen_heatmap(res_x,res_y,height,width,url, **kwargs):
	return db_generate_heatmap.delay(res_x,res_y,height,width,url,**kwargs)
