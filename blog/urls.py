from django.conf.urls import patterns, url, include
from django.conf import settings

urlpatterns = patterns('blog.views',
    (r'article/(?P<artid>\d+)/$', 'article'),
    (r'art/(?P<transition>\w+)/(?P<artid>\d+)/$', 'transition'),
    (r'redactorimagejson/$', 'redactorimagejson'),
    (r'uploadimagejson/$', 'uploadimagejson'),
    (r'search/$', 'search'),
    (r'articlelist.*$', 'blogtermpage', {'termslug' : None}),
    (r't/(?P<termslug>\w+)$', 'blogtermpage'),
    (r't/(?P<termslug>\w+)/$', 'blogtermpage'),
    (r'' , 'blogtermpage', {'termslug' : None}),
)