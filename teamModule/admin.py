from django.contrib import admin
from .models import Formation, Team, Project, Member, ProjectStatus, TeamRole, MemberExtraInfo, MemberExtraInfoType, TeamDisplayView


class PageTeamAdmin(admin.ModelAdmin):
    pass


class PageProjectsAdmin(admin.ModelAdmin):
    pass


class ExtraInfoInline(admin.StackedInline):
    model = MemberExtraInfo
    extra = 0
    fk_name = 'member'


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
    model = TeamDisplayView


class PageMemberExtraInfoAdmin(admin.ModelAdmin):
    pass


class PageMemberExtraInfoTypeAdmin(admin.ModelAdmin):
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
