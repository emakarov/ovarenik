from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

#urlpatterns = i18n_patterns('',
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^photologue/', include('photologue.urls')),
    (r'^projects.*$', 'blog.views.projects'),
    (r'^$', 'blog.views.index'),
    (r'^(?P<artid>.*)/$', 'blog.views.article'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        (r'^favicon.ico', 'serve', {'path' : 'favicon.png'}),
        url(r'^static/(?P<path>.*)$', 'serve'),
        url(r'^[a-z][a-z]/static/(?P<path>.*)$', 'serve'),
        url(r'^media/(?P<path>.*)$', 'serve'),
        )

#if settings.DEBUG:
#    urlpatterns = patterns('',
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#    url(r'', include('django.contrib.staticfiles.urls')),
#) + urlpatterns