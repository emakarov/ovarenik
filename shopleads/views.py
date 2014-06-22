#!
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import Template,RequestContext, loader, Context
from django.conf import settings
from django.contrib.auth.decorators import login_required
from photologue.models import Photo
from django.http import HttpResponse
# Create your views here.
from datetime import tzinfo, timedelta, datetime
from django.views.decorators.cache import never_cache
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.translation import ugettext_noop
from django.utils.translation import get_language
from django.db.models import Q,F
import models as leads_models
from django.core import serializers
from django.utils import simplejson
from django.http import QueryDict
from django.core import mail

def sendreply(request):
    subj = _("Request from site")
    lead = leads_models.Lead()
    leadform = request.POST.get('leadform',None)
    leadformtemplate = loader.get_template(settings.LEADS_TEMPLATES[leadform])
    leadcontent = {}
    for l in request.POST.lists():
      leadcontent[l[0]] = l[1][0]
    c = Context({ 'leadcontent' : leadcontent})
    message = leadformtemplate.render(c)
    try:
      mail.send_mail(subj, message, "info@varenikolga.ru" , ["evgeni.makarov@gmail.com"] )
    except:
      pass
    lead.content = message
    lead.save()
    return render_to_response('email_send.html', [], context_instance = RequestContext(request))
