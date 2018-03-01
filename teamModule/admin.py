from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Formation, Team, Project, Member, ProjectStatus, TeamRole, MemberExtraInfo, MemberExtraInfoType


# Register your models here.
class PageTeamAdmin(admin.ModelAdmin):
    pass


class PageProjectsAdmin(admin.ModelAdmin):
    pass


# class ExtraInfoInline(admin.StackedInline):
#    model = Member.extraInfos.through
#   extra = 1

class ExtraInfoFormSet(BaseInlineFormSet):
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            criteria = {}  # Your criteria here
            qs = super(ExtraInfoFormSet, self).get_queryset().filter(**criteria)
            self._queryset = qs
        return self._queryset


class ExtraInfoInline(admin.StackedInline):
    model = MemberExtraInfo
    extra = 0
    fk_name = 'member'
    formset = ExtraInfoFormSet


class PageMemberAdmin(admin.ModelAdmin):
    model = Member
    inlines = (ExtraInfoInline,)
    exclude = ("extraInfos",)


class PageFormationAdmin(admin.ModelAdmin):
    pass


class PageStatusAdmin(admin.ModelAdmin):
    pass


class PageTeamRoleAdmin(admin.ModelAdmin):
    pass


class PageMemberExtraInfoAdmin(admin.ModelAdmin):
    pass


class PageMemberExtraInfoTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, PageTeamAdmin)
admin.site.register(Project, PageProjectsAdmin)
admin.site.register(Member, PageMemberAdmin)
admin.site.register(Formation, PageFormationAdmin)
admin.site.register(ProjectStatus, PageStatusAdmin)
admin.site.register(TeamRole, PageTeamRoleAdmin)
admin.site.register(MemberExtraInfo, PageMemberExtraInfoAdmin)
admin.site.register(MemberExtraInfoType, PageMemberExtraInfoTypeAdmin)
