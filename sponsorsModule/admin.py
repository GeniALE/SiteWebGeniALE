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

class PageCategoryTranslation(TranslatableAdmin, admin.ModelAdmin):
    pass


admin.site.register(Sponsor, PageSponsorAdmin)
admin.site.register(SponsorsDisplayView, PageSponsorsDisplayView)
admin.site.register(Category, PageCategory)
admin.site.register(CategoryTranslation, PageCategoryTranslation)
