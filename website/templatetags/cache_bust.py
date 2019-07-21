from django import template
from django.conf import settings
import os
import uuid

register = template.Library()


# Inspired from: https://stackoverflow.com/questions/27911070/django-wont-refresh-staticfiles

@register.simple_tag(name='cache_bust')
def cache_bust():
  if settings.DEBUG:
    version = uuid.uuid1()
  else:
    version = os.environ.get('PROJECT_VERSION')
    if version is None:
      version = '1'

  return 'v={version}'.format(version=version)
