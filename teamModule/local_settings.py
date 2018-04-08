from django.conf import settings

TEAMMODULE_TEAMDISPLAY_TEMPLATES = getattr(settings, 'TEAMMODULE_TEAMDISPLAY_TEMPLATES', [
    ('teamModule/team_display.html', 'team_display.html'),
])

TEAMMODULE_TEAMBANNER_TEMPLATES = getattr(settings, 'TEAMMODULE_TEAMBANNER_TEMPLATES', [
    ('teamModule/member_banner.html', 'Default'),
])