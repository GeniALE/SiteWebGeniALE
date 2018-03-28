from django.conf import settings

TEAMMODULE_TEAMDISPLAY_TEMPLATES = getattr(settings, 'TEAMMODULE_TEAMDISPLAY_TEMPLATES', [
    ('teamModule/team_display.html', 'team_display.html'),
    ('teamModule/project_display.html', 'project_display.html'),
])
