from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Page(models.Model):
    """ The Page we want to analyze """
    url = models.URLField(verify_exists=False)
    res_x = models.IntegerField()
    res_y = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
    
    def __unicode__(self):
        return "%s @ %dx%d" % (self.url, self.res_x,self.res_y)        

class ClickItem(models.Model):
    """ A click associated to a Page we want to analize """ 
    page = models.ForeignKey(Page)
    x = models.IntegerField()
    y = models.IntegerField()
    created = models.DateTimeField(_('created'), default=timezone.now, null=True)

