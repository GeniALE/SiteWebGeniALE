from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
import json
from .models import TeamDisplay
from .models import Team
from .models import Member


@plugin_pool.register_plugin
class TeamModulePlugin(CMSPluginBase):
    name = _("Team display plugin")
    model = TeamDisplay
    render_template = "team_display.html"
    cache = False

    def render(self, context, instance, placeholder):
        teams = list(Team.objects.all().order_by("team_name"))
        teams.insert(0, Team(team_name="All"))

        members = Member.objects.select_related()

        context = super(TeamModulePlugin, self).render(context, instance, placeholder)
        context.update({
            'teams': teams,
            'members': serializers.serialize("json", members)
        })
        return context
