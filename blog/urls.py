from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('blog.views',
    (r'article/(?P<artid>\d+)/$', 'article'),
    (r'redactorimagejson/$', 'redactorimagejson'),
    (r'uploadimagejson/$', 'uploadimagejson'),
    (r'search/$', 'search'),
    (r'articlelist.*$', 'blogtermpage', {'termslug' : None}),
    (r't/(?P<termslug>\w+)$', 'blogtermpage'),
    (r't/(?P<termslug>\w+)/$', 'blogtermpage'),
    (r'' , 'blogtermpage', {'termslug' : None}),
)