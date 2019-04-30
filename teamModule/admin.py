from django.contrib import admin
from django.forms import BaseInlineFormSet
from hvad.admin import TranslatableAdmin

from .models import Formation, Team, Project, Member, ProjectStatus, TeamRole, MemberExtraInfo, MemberExtraInfoType, \
    TeamDisplayView, TeamBannerModel, TeamBannerTranslationModel, TeamDisplayTranslationModel, ProjectImage, \
    ProjectDisplayTranslationModel


def get_member_extra_info(user):
    if not user:
        return []
    return list(MemberExtraInfo.objects.filter(member=user))


def get_default_extra_types():
    return [{'info_type': x.id} for x in list(MemberExtraInfoType.objects.all())]


class PageTeamAdmin(admin.ModelAdmin):
    pass


class ProjectPictureInline(admin.StackedInline):
    model = ProjectImage
    extra = 0
    fk_name = 'project'


class PageProjectsAdmin(admin.ModelAdmin):
    model = Member
    inlines = (ProjectPictureInline,)


class ExtraInfoInlineFormSet(BaseInlineFormSet):
    model = MemberExtraInfo

    def __init__(self, *args, **kwargs):
        super(ExtraInfoInlineFormSet, self).__init__(*args, **kwargs)
        self.initial = get_default_extra_types()


class ExtraInfoInline(admin.TabularInline):
    model = MemberExtraInfo
    fk_name = 'member'
    extra = 3
    formset = ExtraInfoInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(ExtraInfoInline, self).get_formset(request, obj, **kwargs)
        member_extra_info = get_member_extra_info(obj)
        default_extra_info = []
        already_defined_info_types = [x.info_type for x in member_extra_info]

        for x in get_default_extra_types():
            if not x in already_defined_info_types:
                default_extra_info.append({'info_type': x})

        formset.initial = default_extra_info
        return formset

    def get_extra(self, request, obj=None, **kwargs):
        member_extra_infos = get_member_extra_info(obj)
        return len(get_default_extra_types()) - len(member_extra_infos)


class PageMemberAdmin(admin.ModelAdmin):
    model = Member
    inlines = (ExtraInfoInline,)
    filter_horizontal = ("teamRoles", "projects",)


class PageFormationAdmin(admin.ModelAdmin):
    pass


class PageStatusAdmin(admin.ModelAdmin):
    pass


class PageTeamRoleAdmin(admin.ModelAdmin):
    pass


"""
Plugins admins
"""


class TeamDisplayViewAdmin(admin.ModelAdmin):
    pass


class TeamBannerAdmin(admin.ModelAdmin):
    pass


class TeamBannerTranslationModelAdmin(TranslatableAdmin, admin.ModelAdmin):
    pass


class TeamDisplayTranslationModelAdmin(TranslatableAdmin, admin.ModelAdmin):
    pass


class PageMemberExtraInfoAdmin(admin.ModelAdmin):
    pass


class PageMemberExtraInfoTypeAdmin(admin.ModelAdmin):
    pass


class ProjectTranslationModelAdmin(TranslatableAdmin, admin.ModelAdmin):
    pass


admin.site.register(ProjectStatus, PageStatusAdmin)
admin.site.register(Formation, PageFormationAdmin)
admin.site.register(Team, PageTeamAdmin)
admin.site.register(Project, PageProjectsAdmin)

admin.site.register(TeamRole, PageTeamRoleAdmin)
admin.site.register(MemberExtraInfo, PageMemberExtraInfoAdmin)
admin.site.register(MemberExtraInfoType, PageMemberExtraInfoTypeAdmin)
admin.site.register(Member, PageMemberAdmin)

admin.site.register(TeamDisplayView, TeamDisplayViewAdmin)
admin.site.register(TeamBannerModel, TeamBannerAdmin)
admin.site.register(TeamBannerTranslationModel, TeamBannerTranslationModelAdmin)
admin.site.register(TeamDisplayTranslationModel, TeamDisplayTranslationModelAdmin)

admin.site.register(ProjectDisplayTranslationModel, ProjectTranslationModelAdmin)
