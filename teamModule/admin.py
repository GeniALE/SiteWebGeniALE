from django.contrib import admin
from django.forms import BaseInlineFormSet, Textarea
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
    model = Team


class ProjectPictureInline(admin.StackedInline):
    model = ProjectImage
    extra = 0
    fk_name = 'project'


class ProjectAdmin(TranslatableAdmin):
    model = Project
    inlines = (ProjectPictureInline,)

    important_fields = ('name', 'visible', 'display_order', 'display_banner_height')
    search_fields = important_fields
    list_display = important_fields


class ExtraInfoInlineFormSet(BaseInlineFormSet):
    model = MemberExtraInfo

    def __init__(self, *args, **kwargs):
        # We get the default values that are not already assigned.
        member_extra_info = get_member_extra_info(kwargs['instance'])
        default_extra_info = []
        already_defined_info_types = [x.info_type.id for x in member_extra_info]

        for x in get_default_extra_types():
            if not x['info_type'] in already_defined_info_types:
                default_extra_info.append(x)

        kwargs['initial'] = default_extra_info
        super(ExtraInfoInlineFormSet, self).__init__(*args, **kwargs)


class ExtraInfoInline(admin.TabularInline):
    model = MemberExtraInfo
    fk_name = 'member'
    extra = 3
    formset = ExtraInfoInlineFormSet

    def get_extra(self, request, obj=None, **kwargs):
        member_extra_infos = get_member_extra_info(obj)
        return len(get_default_extra_types()) - len(member_extra_infos)


class MemberAdmin(TranslatableAdmin):
    model = Member
    inlines = (ExtraInfoInline,)
    filter_horizontal = ("teamRoles", "projects",)

    important_fields = ('first_name', 'last_name', 'email', 'date_joined', 'date_left')
    search_fields = important_fields
    list_display = important_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(MemberAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'bio':
            formfield.widget = Textarea(attrs=formfield.widget.attrs)
        return formfield


class FormationAdmin(TranslatableAdmin):
    model = Formation


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
admin.site.register(ProjectDisplayView, ProjectDisplayViewAdmin)
