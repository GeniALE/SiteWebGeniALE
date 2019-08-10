# -*- coding: utf-8 -*-
import os
import dj_database_url
from dotenv import load_dotenv

_ = lambda s: s
load_dotenv()

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = (os.path.join(BASE_DIR, 'website', 'locale'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(int(os.environ.get('DEBUG', default="0")))
ADMINS = ['root', 'admin']

ALLOWED_HOSTS = [
  "geniale-dev.herokuapp.com",
  "geniale-cms.herokuapp.com",
  "geniale-prod.herokuapp.com",
  "cms.geniale.ca",
  'geniale.ca',
  "web.geniale.ca",
  "localhost",
  "127.0.0.1"
]

docker_toolbox = os.getenv("DOCKERHOST")

if docker_toolbox:
  ALLOWED_HOSTS.append(docker_toolbox)

# Email configuration
raw_email_use_ssl = os.getenv('EMAIL_USE_SSL', 0)
raw_email_use_tls = os.getenv('EMAIL_USE_TLS', 0)
raw_email_port = os.getenv('EMAIL_PORT', 25)

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_PORT = int(raw_email_port)
EMAIL_USE_SSL = bool(int(raw_email_use_ssl))
EMAIL_USE_TLS = bool(int(raw_email_use_tls))

# Application definition

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'website', 'static'),
  os.path.join(BASE_DIR, 'teamModule', 'static'),
)
#http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'website', 'templates'), ],
    'OPTIONS': {
      'context_processors': [
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.template.context_processors.i18n',
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.template.context_processors.media',
        'django.template.context_processors.csrf',
        'django.template.context_processors.tz',
        'sekizai.context_processors.sekizai',
        'django.template.context_processors.static',
        'cms.context_processors.cms_settings'
      ],
      'loaders': [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader'
      ],
    },
  },
]

MIDDLEWARE_CLASSES = (
  'cms.middleware.utils.ApphookReloadMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'cms.middleware.user.CurrentUserMiddleware',
  'cms.middleware.page.CurrentPageMiddleware',
  'cms.middleware.toolbar.ToolbarMiddleware',
  'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
  # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
  'whitenoise.runserver_nostatic', #to get whitenoise to server static in dev too
  'djangocms_admin_style',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.admin',
  'django.contrib.sites',
  'django.contrib.sitemaps',
  'django.contrib.staticfiles',
  'django.contrib.messages',
  'cms',
  'menus',
  'sekizai',
  'treebeard',
  'djangocms_text_ckeditor',
  'filer',
  'easy_thumbnails',
  'djangocms_column',
  'djangocms_file',
  'djangocms_link',
  'djangocms_picture',
  'djangocms_style',
  'djangocms_snippet',
  'djangocms_googlemap',
  'djangocms_video',
  'website',
  'adminsortable',
  'cmsplugin_contact_plus',
  'compressor',
  'hvad',
  'teamModule',
  'sponsorsModule',
  'beer_carousel'
)

LANGUAGES = (
  ## Customize this
  ('fr', _('fr')),
  ('en', _('en')),
)

CMS_LANGUAGES = {
  ## Customize this
  'default': {
    'redirect_on_fallback': True,
    'public': True,
    'hide_untranslated': False,
  },
  1: [
    {
      'code': 'fr',
      'name': _('French'),
      'fallbacks': ['en'],
      'redirect_on_fallback': True,
      'public': True,
      'hide_untranslated': False,
    },
    {
      'code': 'en',
      'name': _('English'),
      'redirect_on_fallback': True,
      'public': True,
      'hide_untranslated': False,
    },
  ],

}

CMS_TEMPLATES = (
  ## Customize this
  ('fullwidth.html', 'Fullwidth'),
  ('sidebar_left.html', 'Sidebar Left'),
  ('sidebar_right.html', 'Sidebar Right'),
  ('landing_page.html', 'Landing Page'),
  ('404.html', 'Error page')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('POSTGRES_DB', 'postgres'),
    'USER': os.getenv('POSTGRES_USER', 'postgres'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'geniale'),
    'HOST': os.getenv('POSTGRES_HOST', 'db'),
    'PORT': os.getenv('POSTGRES_PORT', '5432'),
  }
}

db_url = os.getenv('DATABASE_URL', False)
if db_url:
  DATABASES['default'] = dj_database_url.parse(db_url)

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
  'easy_thumbnails.processors.colorspace',
  'easy_thumbnails.processors.autocrop',
  'filer.thumbnail_processors.scale_and_crop_with_subject_location',
  'easy_thumbnails.processors.filters'
)

CMSPLUGIN_CONTACT_PLUS_TEMPLATES = [
  ('components/contact.html', 'Geniale contact form'),
  ('cmsplugin_contact_plus/contact.html', 'Default contact form'),
]

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  # other finders..
  'compressor.finders.CompressorFinder'
)

TEAMMODULE_TEAMDISPLAY_TEMPLATES = [
  ('teamModule/team_display.html', 'Default'),
  ('components/member_count.html', 'Total member count'),
  ('components/team_display.html', 'Team member display')
]

TEAMMODULE_TEAMBANNER_TEMPLATES = [
  ('teamModule/member_banner.html', 'Default'),
  ('components/member_banner.html', 'Team banner'),
]

SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES = [
  ('sponsorsModule/sponsors_display.html', 'Default'),
  ('components/sponsors_display.html', 'Sponsors Display')
]

BEER_CAROUSEL_TEMPLATES_TEMPLATES = [
  ('beer_carousel/default.html', 'Default'),
  ('components/beer_carousel.html', 'Custom beer template'),
]

TEAMMODULE_PROJECTDISPLAY_TEMPLATES = [
  ('teamModule/project_display.html', 'List projects')
]

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter']
COMPRESS_ENABLED = not DEBUG

COMPRESS_JS_FILTERS = [
  'compressor.filters.jsmin.SlimItFilter'
]

COMPRESS_PRECOMPILERS = (
  ('text/x-scss', 'django_libsass.SassCompiler'),
)

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'ERROR',
      'propagate': True,
    },
    'django.db.backends': {
      'level': 'INFO',
    },
  }
}
