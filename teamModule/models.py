from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from cms.models.fields import PlaceholderField
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
from teamModule import local_settings


class Formation(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.team_name


class TeamRole(models.Model):
    role = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.role + ' (' + self.team.team_name + ')'


class ProjectStatus(models.Model):
    status = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "project statuses"


class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, null=True)
    status = models.ForeignKey(ProjectStatus, default=0, on_delete=models.SET_DEFAULT)
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.project_name


class Member(models.Model):
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    bio = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=75)
    linkedInUrl = models.CharField(max_length=200, blank=True)
    profilePicUrl = models.CharField(max_length=200, blank=True)
    formation = models.ForeignKey(Formation, null=True, on_delete=models.SET_NULL)
    teamRoles = models.ManyToManyField(TeamRole)
    projects = models.ManyToManyField(Project)

    # extraInfos= models.ManyToManyField(MemberExtraInfo)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class MemberExtraInfoType(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.description)


class MemberExtraInfo(models.Model):
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    info_type = models.ForeignKey(MemberExtraInfoType, default=0, on_delete=models.SET_DEFAULT)
    value = models.CharField(max_length=500)

    def __str__(self):
        return "{} {}".format(self.info_type, self.value)


"""
Plugins models
"""


@python_2_unicode_compatible
class TeamDisplayView(CMSPlugin):
    template = models.CharField(
        max_length=255,
        choices=local_settings.TEAMMODULE_TEAMDISPLAY_TEMPLATES,
        default='teamModule/team_display.html',
        editable=len(local_settings.TEAMMODULE_TEAMDISPLAY_TEMPLATES) > 1)
    css_class_prefix = models.CharField(
        max_length=100,
        default="",
        blank=True
    )

    select_all_text = models.CharField(
        max_length=100,
        default="All"
    )

    class Meta:
        verbose_name = "TeamModule Team Display"
        verbose_name_plural = "TeamModule Team Displays"


@python_2_unicode_compatible
class TeamBannerTranslationModel(TranslatableModel):
    translations = TranslatedFields(
        members=models.CharField(max_length=255),
        member_description=models.CharField(max_length=255),
        member_more_detail=models.CharField(max_length=255),
    )

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"


@python_2_unicode_compatible
class TeamBannerModel(CMSPlugin):
    template = models.CharField(
        max_length=255,
        choices=local_settings.TEAMMODULE_TEAMBANNER_TEMPLATES,
        default='teamModule/member_banner.html',
        editable=len(local_settings.TEAMMODULE_TEAMBANNER_TEMPLATES) > 1)
    translations = models.ForeignKey(TeamBannerTranslationModel)
    team_image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name = "TeamModule Team Banner"
        verbose_name_plural = "TeamModule Team Banners"
