from django.contrib import admin
from .models import Formation, Team, Project, Member


# Register your models here.
class PageTeamAdmin(admin.ModelAdmin):
    pass


class PageProjectsAdmin(admin.ModelAdmin):
    pass


class PageMemberAdmin(admin.ModelAdmin):
    pass


class PageFormationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, PageTeamAdmin)
admin.site.register(Project, PageProjectsAdmin)
admin.site.register(Member, PageMemberAdmin)
admin.site.register(Formation, PageFormationAdmin)
