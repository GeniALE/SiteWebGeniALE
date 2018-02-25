from collections import OrderedDict

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.forms import model_to_dict
from django.utils.translation import ugettext_lazy as _
from django.core import serializers
import json

from teamModule.helpers import to_dict
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
        teams.insert(0, Team(id=-1, team_name="All"))

        members = Member.objects.prefetch_related(
            'teamRoles__team',
            'formation'
        )

        members_as_dict = []
        teams_as_dict = {team.id: model_to_dict(team) for team in teams}
        for (team_id, team) in teams_as_dict.items():
            teams_as_dict[team_id]['members_count'] = 0

        # All special case
        teams_as_dict[-1]['members_count'] = len(members)
        teams_as_dict = OrderedDict(sorted(teams_as_dict.items(), key=lambda t: t[0]))

        for member in members:
            new_member = to_dict(member)
            teamRoles = member.teamRoles.all()

            # Increment team count
            for teamRole in teamRoles:
                teams_as_dict[teamRole.team_id]['members_count'] += 1
            new_member['teamRoles'] = [to_dict(teamRole) for teamRole in teamRoles]
            new_member['projects'] = [to_dict(project) for project in member.projects.all()]
            new_member['formation'] = to_dict(member.formation)
            members_as_dict.append(new_member)

        context = super(TeamModulePlugin, self).render(context, instance, placeholder)
        context.update({
            'teams': list(teams_as_dict.values()),
            'members': members,
            'teamsAsJson': json.dumps(list(teams_as_dict.values())),
            'membersAsJson': json.dumps(members_as_dict),
            'prefix': 'teamModule__'
        })
        return context
