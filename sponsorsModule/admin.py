from django.contrib import admin

from .models import Sponsor, SponsorsDisplayView, Category, CategoryTranslation, SponsorsDisplayViewTranslations
from hvad.admin import TranslatableAdmin


class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor

    important_fields = ('title', 'url', 'score')
    search_fields = important_fields
    list_display = important_fields


class SponsorsDisplayViewAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)


class CategoryAdmin(admin.ModelAdmin):
    pass


class CategoryTranslationAdmin(TranslatableAdmin, admin.ModelAdmin):
    pass


class SponsorsDisplayViewTranslationsAdmin(TranslatableAdmin, admin.ModelAdmin):
    pass


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryTranslation, CategoryTranslationAdmin)

admin.site.register(SponsorsDisplayView, SponsorsDisplayViewAdmin)
admin.site.register(SponsorsDisplayViewTranslations, SponsorsDisplayViewTranslationsAdmin)
