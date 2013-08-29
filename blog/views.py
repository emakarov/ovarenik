# coding=utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template,RequestContext, loader, Context
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from datetime import tzinfo, timedelta, datetime
from django.views.decorators.cache import never_cache
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.translation import ugettext_noop
from django.utils.translation import get_language
from blog import models as blog_models
from django.db.models import Q,F
from photologue.models import ImageModel, Gallery, Photo
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import random
import string
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import mail

blog_index_html = settings.BLOG_INDEX_HTML
blog_articlelist_html = settings.BLOG_ARTICLELIST_HTML
blog_article_html = settings.BLOG_ARTICLE_HTML
blog_projects_html = settings.BLOG_PROJECTS_HTML

def index(request):
  g = Gallery.objects.get(title_slug="mainpagebackground")
  p = g.photos.all().order_by('?')[0]
  return render_to_response(blog_index_html, {'photo' : p }, context_instance = RequestContext(request))
  
def blogtermpage(request,termslug):
  if termslug is not None:
    term = blog_models.Term.objects.filter(termslug = termslug)
    article_list = blog_models.Article.objects.filter(terms__in = term, publish_status = '2').exclude(cover=None)
  else:
    article_list = blog_models.Article.objects.filter(publish_status = '2').exclude(cover=None)
  terms = blog_models.Term.objects.all().exclude(is_servicecat=True)
  paginator = Paginator(article_list, 5) # Show 5 articles per page
  page = request.GET.get('page',1)
  try:
    articles = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    articles = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    articles = paginator.page(paginator.num_pages)
  page_range = paginator.page_range
  params = { 'articles' : articles, 'page_range' : page_range, 'terms' : terms }
  return render_to_response(blog_articlelist_html, params, context_instance = RequestContext(request))

def search(request):
    q = None
    try:
      q = request.GET['s']
    except:
      pass
    if q:
      articles = blog_models.Article.objects.filter(Q(title__icontains=q) | Q(text__icontains=q), publish_status = '2')
    else:
      articles = blog_models.Article.all().none()
    terms = blog_models.Term.objects.all().exclude(is_servicecat=True)
    params = { 'articles' : articles, 'terms' : terms }
    return render_to_response(blog_articlelist_html(request), params, context_instance = RequestContext(request))
  
def article(request,artid):
  try:
    article = blog_models.Article.objects.get(id=artid)
  except:
    article = blog_models.Article.objects.get(slug=artid)
  sidebar = blog_models.Article.objects.filter(publish_status = '2').exclude(id=article.id).order_by('?')[0:20]
  terms = blog_models.Term.objects.all().exclude(is_servicecat=True)
  params = { 'article' : article, 'sidebar' : sidebar, 'terms' : terms }
  return render_to_response(article.template, params, context_instance = RequestContext(request))

def transition(request,transition,artid):
  a = blog_models.Article.objects.get(id=artid)
  term = a.terms.all()[0]
  a_t = blog_models.Article.objects.filter(terms = term)
  if transition == "next":
    try:
      article = a_t.filter(id__gt=a.id).order_by('id')[0]
    except:
      article = a_t.order_by('id')[0]
  else:
    try:
      article = a_t.filter(id__lt=a.id).order_by('-id')[0]
    except:
      article = a_t.order_by('-id')[0]
  return redirect("/%s/" % article.slug)


def projects(request):
  term = blog_models.Term.objects.filter(termslug='projects') #reserved for projects
  articles = blog_models.Article.objects.filter(terms__in = term, publish_status = '2').exclude(cover=None)
  galleries = Gallery.objects.filter(gallery_articles__in=articles)
  photos = Photo.objects.filter(galleries__in=galleries).order_by('?').select_related('galleries__gallery_articles')
  photos18 = photos[0:18]
  params = { 'articles' : articles, 'photos' : photos, 'photos18' : photos18 }
  return render_to_response(blog_projects_html, params, context_instance = RequestContext(request))
  
def redactorimagejson(request):
  photos = Photo.objects.all().order_by('-id')
  template = loader.get_template('redactorimagesjson.html')
  params = { 'photos' : photos }
  context = RequestContext(request, params)  
  return HttpResponse(template.render(context),mimetype='application/json')  

@csrf_exempt  
def uploadimagejson(request):
  p = Photo()
  if request.user.is_authenticated():
    if request.method == 'POST':
      pt = codegenerator()+codegenerator()
      p.image = request.FILES['file']
      p.title = pt
      p.title_slug = slugify(pt) #+codegenerator()
      p.save()
#  template = loader.get_template('redactorimageupload.html')
    params = { 'photo' : p }
#  context = RequestContext(request, params)  
  return render_to_response('redactorimageupload.html',params,context_instance = RequestContext(request))
#  return HttpResponse(template.render(context),mimetype='application/json')  
        
    
def codegenerator():
  digits = "".join( [random.choice(string.digits) for i in xrange(3)] )
  chars = "".join( [random.choice(string.letters) for i in xrange(4)] ).lower()
  digits2 = "".join( [random.choice(string.digits) for i in xrange(3)] )
  return digits+chars+digits2

def sendmail(request):
    #email_to = 'olgavarenik@gmail.com'
    email_to = 'evgeni.makarov@gmail.com'
    ue = request.POST['name']
    text = request.POST['text']
    email = request.POST['email']
    subj = u'Отзыв с сайта Ольги Вареник' #request.POST['subj']
    message = text+u'\nИмя пользователя:'+ue+u'\nEmail пользователя:'+email
    mail.send_mail(subj, message, 'site@olgavarenik.ru', [ email_to ])
    mail.send_mail(subj, message, 'site@olgavarenik.ru', [ 'vj.workshop@gmail.com' ])
    mail.send_mail(subj, message, 'site@olgavarenik.ru', [ 'olgavarenik@gmail.com' ])
    #print message
    return render_to_response('email_send.html', [], context_instance = RequestContext(request))