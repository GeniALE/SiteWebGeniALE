#!/usr/bin/python

from django.conf import settings

SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES = getattr(settings, 'SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES', [
    ('sponsorsModule/sponsors_display.html', 'sponsors_display.html'),
])
#
# TEAMMODULE_TEAMBANNER_TEMPLATES = getattr(settings, 'TEAMMODULE_TEAMBANNER_TEMPLATES', [
#     ('sponsorsModule/member_banner.html', 'Default'),
# ])
