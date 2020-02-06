from collections import OrderedDict
from django.core.serializers.json import DjangoJSONEncoder
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
import json
from django.templatetags.static import static

from teamModule.helpers import to_dict
from .models import TeamBannerModel, Team, Member, TeamDisplayView, Project, ProjectDisplayView

get_member_filter = Q(date_left__isnull=True) | Q(date_left__gt=timezone.now())


@plugin_pool.register_plugin
class TeamModulePlugin(CMSPluginBase):
    name = _("Team display plugin")
    model = TeamDisplayView
    render_template = "teamModule/team_display.html"
    cache = False

    def get_members(self):
        members = Member.objects.language().filter(get_member_filter).prefetch_related(
            'teamRoles__team',
            'formation',
            'translations'
        ).order_by("first_name")
        return members

    def get_teams(self, instance):
        teams = list(Team.objects.language().all().order_by("team_name"))
        teams.sort(key=lambda team: team.team_name)

        all_text = instance.translations.all
        teams.insert(0, Team(id=-1, team_name=all_text))
        return teams

    def members_to_dict(self, members):
        members_as_dict = []
        for member in members:
            new_member = to_dict(member, ['bio'])
            team_roles = member.teamRoles.all()
            new_member['teamRoles'] = [to_dict(teamRole, ['role']) for teamRole in team_roles]
            new_member['projects'] = [to_dict(project, ['description']) for project in member.projects.all()]
            new_member['formation'] = to_dict(member.formation, ['name', 'url'])
            members_as_dict.append(new_member)

        return members_as_dict

    def teams_to_dict(self, teams, members):
        teams_as_dict = {team.id: to_dict(team, ['team_name']) for team in teams}
        for (team_id, team) in teams_as_dict.items():
            teams_as_dict[team_id]['members_count'] = 0

        for member in members:
            team_roles = member.teamRoles.all()
            for teamRole in team_roles:
                teams_as_dict[teamRole.team_id]['members_count'] += 1

        # Add the "All" team special case
        teams_as_dict[-1]['members_count'] = len(members)

        # Remove team without any members
        teams_as_dict = {key: val for key, val in teams_as_dict.items() if val['members_count'] > 0}

        # Sort teams
        teams_as_dict = OrderedDict(sorted(teams_as_dict.items(), key=lambda t: t[0]))
        return teams_as_dict

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(TeamModulePlugin, self).render(context, instance, placeholder)

        # Get some data
        members = self.get_members()

        # Check for default avatar
        for member in members:
            if not member.image:
                member.image = static("image/default_avatar.png")
            else:
                member.image = member.image.url

        teams = self.get_teams(instance)
        members_as_dict = self.members_to_dict(members)
        teams_as_dict = self.teams_to_dict(teams, members)
        ordered_teams_for_ui = sorted(list(teams_as_dict.values()), key=lambda team: team['team_name'])

        # Replace the all_team to the first place
        all_team = next(x for x in ordered_teams_for_ui if x['id'] == -1)
        ordered_teams_for_ui.remove(all_team)
        ordered_teams_for_ui.insert(0, all_team)

        context.update({
            'teams': ordered_teams_for_ui,
            'members': members,
            'teamsAsJson': json.dumps(list(teams_as_dict.values())),
            'membersAsJson': json.dumps(members_as_dict, cls=DjangoJSONEncoder),
            'uniqueName': 'teamModuleDisplay' + '__' + str(instance.id),
            'translations': instance.translations,
            'cssPrefix': instance.css_class_prefix
        })
        return context


@plugin_pool.register_plugin
class ProjectModulePlugin(CMSPluginBase):
    name = _("Project display plugin")
    model = ProjectDisplayView
    render_template = "projectModule/project_display.html"
    cache = False

    def get_projects(self):
        projects = Project.objects.language().filter(visible=True).order_by('display_order').prefetch_related(
            'status', 'images'
        )
        return projects

    def projects_to_dict(self, projects):
        # projects_as_dict = {project.id: model_to_dict(project) for project in projects}

        projects_as_dict = []
        for project in projects:
            new_project = to_dict(project, ['description'])
            images = project.images.all()
            new_images = []
            for image_obj in images:
                new_image = str(image_obj)
                new_images.append(new_image)
            new_project['images'] = new_images
            new_project['status_text'] = project.status.status
            projects_as_dict.append(new_project)

        return projects_as_dict

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(ProjectModulePlugin, self).render(context, instance, placeholder)

        # Get some data
        projects = self.get_projects()
        projects_to_dict = self.projects_to_dict(projects)

        context.update({
            'projects': projects,
            'projectsAsJson': json.dumps(projects_to_dict),
            'uniqueName': 'projectModuleDisplay' + '__' + str(instance.id),
            'translations': instance.translations,
            'cssPrefix': instance.css_class_prefix,
        })
        return context


@plugin_pool.register_plugin
class TeamBannerPlugin(CMSPluginBase):
    name = _("Team banner plugin")
    model = TeamBannerModel
    render_template = "teamModule/member_banner.html"
    cache = False

    def get_member_count(self):
        return Member.objects.filter(get_member_filter).count()

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(TeamBannerPlugin, self).render(context, instance, placeholder)

        # Get some data
        member_count = self.get_member_count()

        context.update({
            'member_count': json.dumps(member_count),
            'translations': instance.translations,
            'image': instance.team_image,
            'details_button_link': instance.details_button_link
        })
        return context
