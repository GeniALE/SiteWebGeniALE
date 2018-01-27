from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from .models import Formation, Team, Project, Member


# Register your models here.
class PageTeamAdmin(PageExtensionAdmin):
    pass


class PageProjectsAdmin(PageExtensionAdmin):
    pass


class PageMemberAdmin(PageExtensionAdmin):
    pass


class PageFormationAdmin(PageExtensionAdmin):
    pass


admin.site.register(Team, PageTeamAdmin)
admin.site.register(Project, PageProjectsAdmin)
admin.site.register(Member, PageMemberAdmin)
admin.site.register(Formation, PageFormationAdmin)
