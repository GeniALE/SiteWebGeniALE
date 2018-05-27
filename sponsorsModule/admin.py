from django.contrib import admin
from .models import Sponsor, SponsorsDisplayView, Category, CategoryTranslation
from hvad.admin import TranslatableAdmin
#


class PageSponsorAdmin(admin.ModelAdmin):
    model = Sponsor

class PageSponsorsDisplayView(admin.ModelAdmin):
    pass
class PageCategory(admin.ModelAdmin):
    pass

class PageCategoryTranslation(admin.ModelAdmin):
    pass


admin.site.register(Sponsor, PageSponsorAdmin)
admin.site.register(SponsorsDisplayView, PageSponsorsDisplayView)
admin.site.register(Category, PageCategory)
admin.site.register(CategoryTranslation, PageCategoryTranslation)
# admin.site.register(TeamRole, PageTeamRoleAdmin)
# admin.site.register(MemberExtraInfo, PageMemberExtraInfoAdmin)
# admin.site.register(MemberExtraInfoType, PageMemberExtraInfoTypeAdmin)
# admin.site.register(Member, PageMemberAdmin)
#
# admin.site.register(TeamDisplayView, TeamDisplayViewAdmin)
# admin.site.register(TeamBannerModel, TeamBannerAdmin)
# admin.site.register(TeamBannerTranslationModel, TeamBannerTranslationModelAdmin)
# admin.site.register(TeamDisplayTranslationModel, TeamDisplayTranslationModelAdmin)
