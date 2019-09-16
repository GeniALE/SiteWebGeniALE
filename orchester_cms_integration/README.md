# Orchester CMS integration

The Django-CMS integration of the Orchester service library


# Getting started

In your website `settings.py`, you must add the *orchester_cms_integration* in the 
INSTALLED app list after teamModule:

```python

INSTALLED_APPS = (
  'djangocms_admin_style',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.admin',
  /* ... */
  'teamModule',
  'orchester_cms_integration'
)
```

Now in your website `urls.py` file, you'll need to register the app urls:

```python
urlpatterns += i18n_patterns(
  url(r'^admin/', include(admin.site.urls)),  # NOQA
  url(r'^orchester/', include('orchester_cms_integration.urls')),
  url(r'^', include('cms.urls')),
)
```
