from django.contrib import admin
from .models import Formation, Team, Project, Member, ProjectStatus, TeamRole, MemberExtraInfo, MemberExtraInfoType


# Register your models here.
class PageTeamAdmin(admin.ModelAdmin):
    pass


class PageProjectsAdmin(admin.ModelAdmin):
    pass


class PageMemberAdmin(admin.ModelAdmin):
    pass


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
