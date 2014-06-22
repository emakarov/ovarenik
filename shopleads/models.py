from django.db import models
from django.utils.translation import ugettext_lazy as _

class Lead(models.Model):
  content = models.TextField(blank=True, default='', verbose_name=_('Content'), help_text=_('content'))
  received = models.DateTimeField(verbose_name=_("Received"), blank=True, null=True, auto_now_add = True)
            
  def __unicode__(self):
    return self.content
  
  class Meta:
    verbose_name = _("Lead")
    verbose_name_plural = _("Leads")
