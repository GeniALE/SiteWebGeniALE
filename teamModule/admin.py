from django.contrib import admin
from django.forms import BaseInlineFormSet
from hvad.admin import TranslatableAdmin

from .models import Formation, Team, Project, Member, ProjectStatus, TeamRole, MemberExtraInfo, MemberExtraInfoType, \
    TeamDisplayView, TeamBannerModel, TeamBannerTranslationModel, TeamDisplayTranslationModel, ProjectImage, \
    ProjectDisplayTranslationModel, ProjectDisplayView


def get_member_extra_info(user):
    if not user:
        return []
    return list(MemberExtraInfo.objects.filter(member=user))


def get_default_extra_types():
    return [{'info_type': x.id} for x in list(MemberExtraInfoType.objects.all())]


class TeamAdmin(TranslatableAdmin):
    pass


class ProjectPictureInline(admin.StackedInline):
    model = ProjectImage
    extra = 0
    fk_name = 'project'


class ProjectAdmin(TranslatableAdmin):
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


class MemberAdmin(TranslatableAdmin):
    model = Member
    inlines = (ExtraInfoInline,)
    filter_horizontal = ("teamRoles", "projects",)


class FormationAdmin(TranslatableAdmin):
    pass


class StatusAdmin(TranslatableAdmin):
    pass


class TeamRoleAdmin(TranslatableAdmin):
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

class ProjectDisplayViewAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectStatus, StatusAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.register(TeamRole, TeamRoleAdmin)
admin.site.register(MemberExtraInfo, PageMemberExtraInfoAdmin)
admin.site.register(MemberExtraInfoType, PageMemberExtraInfoTypeAdmin)
admin.site.register(Member, MemberAdmin)

admin.site.register(TeamDisplayView, TeamDisplayViewAdmin)
admin.site.register(TeamBannerModel, TeamBannerAdmin)
admin.site.register(TeamBannerTranslationModel, TeamBannerTranslationModelAdmin)
admin.site.register(TeamDisplayTranslationModel, TeamDisplayTranslationModelAdmin)

admin.site.register(ProjectDisplayTranslationModel, ProjectTranslationModelAdmin)
admin.site.register(ProjectDisplayView,ProjectDisplayViewAdmin)
