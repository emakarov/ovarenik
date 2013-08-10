# coding=utf-8

# Django settings for olympics project.
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
#import os
from os import path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

ROOT_DIR = path.abspath(path.dirname(path.abspath(__file__)))
PROJECT_ROOT = ROOT_DIR
PROJECT_DIR = path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ovarenik',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'ovarenik',
        'PASSWORD': 'ovarenik',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

LANGUAGES = (
#        ('en', _('English')),
        ('ru', _('Russian')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''
MEDIA_ROOT = path.join(ROOT_DIR, 'static/')
ADMIN_MEDIA_ROOT = path.join(ROOT_DIR, 'static/admin/')
ADMIN_MEDIA_PREFIX = '/static/admin/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = '/static/'

STATIC_ROOT = STATICFILES_ROOT = path.join(ROOT_DIR,'static')

STATIC_URL = STATICFILES_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mg5-op972k3@qelfbcr#i393q5w4m-dvl9xumt1#)bvf*ey(an'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'setlocalemiddleware.SetLocaleMiddleware',
)

ROOT_URLCONF = 'ovarenik.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ovarenik.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path.join(PROJECT_ROOT,'templates'),
)

LOCALE_PATHS = (
  path.join(PROJECT_ROOT,'locale'),
)
#print LOCALE_PATHS

INSTALLED_APPS = (
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
#    'photologue',
    'django_extensions',
    'mptt',
#    'accounts',
#    'commerce',
#    'ncatalogue',
#    'shops',
#    'social_auth',
    #'tagging',
#    'utils',
#    'django.contrib.comments',
    'sitemanagement',
    'blog',
    'photologue',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.request',
#    'django.core.context_processors.media',
#    'django.core.context_processors.static',
#)

BLOG_INDEX_HTML = 'blog/index.html'
BLOG_ARTICLELIST_HTML = 'blog/articlelist.html'
BLOG_ARTICLE_HTML = 'blog/article.html'
BLOG_PROJECTS_HTML = 'blog/projects.html'

BLOG_TEMPLATES = (
  ('blog/article.html',_("Simple article")),
  ('blog/about.html',_("About page")),
  ('blog/index.html',_("Main page")),
  ('blog/articlelist.html',_("List of articles")),
  ('blog/project.html',_("Design project")),
)


CMS_TEMPLATES = (
    ('index.html', 'Main page'),
)

PHOTOLOGUE_MAXBLOCK = 1024*2**10
