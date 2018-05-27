from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
from sponsorsModule import local_settings


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    def __str__(self):
        return self.name

class CategoryTranslation(models.Model):
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.name

class Sponsor(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='media/')

"""
Plugins models
"""


# @python_2_unicode_compatible
# class TeamDisplayTranslationModel(TranslatableModel):
#     translations = TranslatedFields(
#         teams_title=models.CharField(max_length=255, default="Teams"),
#         all=models.CharField(max_length=255, default="All"),
#         members_title=models.CharField(max_length=255, default="Members"),
#         projects_title=models.CharField(max_length=255, default="Projects"),
#         formation_title=models.CharField(max_length=255, default="Formation"),
#     )
#
#     def __str__(self):
#         return "Team display's translations({})".format(self.id)

    # class Meta:
    #     verbose_name = "TeamDisplay Translation model"
    #     verbose_name_plural = "TeamDisplay Translation models"


# @python_2_unicode_compatible
# class TeamBannerTranslationModel(TranslatableModel):
#     translations = TranslatedFields(
#         members=models.CharField(max_length=255, default="members"),
#         member_description=models.CharField(max_length=255),
#         member_more_detail=models.CharField(max_length=255, default="More details"),
#     )
#
#     def __str__(self):
#         return "Team banner's translations({})".format(self.id)
#
#     class Meta:
#         verbose_name = "TeamBanner Translation model"
#         verbose_name_plural = "TeamBanner Translation models"
#

@python_2_unicode_compatible
class SponsorsDisplayView(CMSPlugin):
    template = models.CharField(
        max_length=255,
        choices=local_settings.SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES,
        default='sponsorsModule/sponsorsmodule_display.html',
        editable=len(local_settings.SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES) > 1)
    css_class_prefix = models.CharField(
        max_length=100,
        default="",
        blank=True
    )

    # translations = models.ForeignKey(TeamDisplayTranslationModel, null=True)

    class Meta:
        verbose_name = "SponsorsModule Sponsors Display"
        verbose_name_plural = "SponsorsModule Sponsors Displays"

#
# @python_2_unicode_compatible
# class TeamBannerModel(CMSPlugin):
#     template = models.CharField(
#         max_length=255,
#         choices=local_settings.TEAMMODULE_TEAMBANNER_TEMPLATES,
#         default='sponsorsModule/member_banner.html',
#         editable=len(local_settings.TEAMMODULE_TEAMBANNER_TEMPLATES) > 1)
#     translations = models.ForeignKey(TeamBannerTranslationModel)
#     team_image = models.ImageField(upload_to='media/')
#
#     class Meta:
#         verbose_name = "TeamModule Team Banner"
#         verbose_name_plural = "TeamModule Team Banners"
