from collections import OrderedDict

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.forms import model_to_dict
from django.utils.translation import ugettext_lazy as _
import json

from sponsorsModule.helpers import to_dict
from .models import CategoryTranslation, Category, Sponsor, SponsorsDisplayView


@plugin_pool.register_plugin
class SponsorsModulePlugin(CMSPluginBase):
    name = _("Sponsors display plugin")
    model = SponsorsDisplayView
    render_template = "sponsorsModule/sponsors_display.html"
    cache = False

    def get_sponsors(self):
        sponsors = list(Sponsor.objects.all().order_by("title"))
        return sponsors

    def get_categories(self,instance):
        categories = list(Category.objects.all().order_by("scoreMin"))
        return categories

    # def sponsors_to_dict(self, sponsors):
    #     sponsors_as_dict = []
    #     for sponsor in members:
    #         new_sponsor = to_dict(member)
    #         team_roles = member.teamRoles.all()
    #         new_sponsor['title'] = [to_dict(teamRole) for teamRole in team_roles]
    #         new_sponsor['url'] = [to_dict(project) for project in member.projects.all()]
    #         new_sponsor['image'] = to_dict(member.formation)
    #         sponsors_as_dict.append(new_member)
    #
    #     return sponsors_as_dict
    #
    # def teams_to_dict(self, teams, members):
    #     teams_as_dict = {team.id: model_to_dict(team) for team in teams}
    #     for (team_id, team) in teams_as_dict.items():
    #         teams_as_dict[team_id]['members_count'] = 0
    #
    #     for member in members:
    #         team_roles = member.teamRoles.all()
    #         for teamRole in team_roles:
    #             teams_as_dict[teamRole.team_id]['members_count'] += 1
    #
    #     # All special case
    #     teams_as_dict[-1]['members_count'] = len(members)
    #     teams_as_dict = OrderedDict(sorted(teams_as_dict.items(), key=lambda t: t[0]))
    #     return teams_as_dict

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(SponsorsModulePlugin, self).render(context, instance, placeholder)

        # Get some data
        sponsors= self.get_sponsors()
        categories = self.get_categories(instance)

        context.update({
            'sponsors': sponsors,
            'cssPrefix': instance.css_class_prefix
        })
        return context

#
# @plugin_pool.register_plugin
# class SponsorsBannerPlugin(CMSPluginBase):
#     name = _("Team banner plugin")
#     model = SponsorsBannerModel
#     render_template = "sponsorsModule/sponsors_banner.html"
#     cache = False
#
#     def get_member_count(self):
#         return Member.objects.count()
#
#     def render(self, context, instance, placeholder):
#         if instance and instance.template:
#             self.render_template = instance.template
#
#         context = super(TeamBannerPlugin, self).render(context, instance, placeholder)
#
#         # Get some data
#         member_count = self.get_member_count()
#
#         context.update({
#             'member_count': json.dumps(member_count),
#             'translations': instance.translations,
#             'image': instance.team_image
#         })
#         return context
