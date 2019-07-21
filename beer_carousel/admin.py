from django.contrib import admin
from hvad.admin import TranslatableAdmin

from .models import BeerCarouselPluginModel, BeerModel, BeerTranslationsModel, BeerCarouselPluginTranslationModel, \
  BeerContainer


class BeerCarouselTranslationModelAdmin(TranslatableAdmin, admin.ModelAdmin):
  pass


class BeerTranslationsAdmin(TranslatableAdmin, admin.ModelAdmin):
  pass


class BeerAdmin(admin.ModelAdmin):
  model = BeerModel

  important_fields = ('name', 'type', 'alcohol_percent', 'ibu', 'created_at')
  search_fields = important_fields
  list_display = important_fields


class BeerPluginAdmin(admin.ModelAdmin):
  pass


class BeerContainerAdmin(admin.ModelAdmin):
  pass


admin.site.register(BeerModel, BeerAdmin)
admin.site.register(BeerCarouselPluginModel, BeerPluginAdmin)

admin.site.register(BeerTranslationsModel, BeerTranslationsAdmin)
admin.site.register(BeerCarouselPluginTranslationModel, BeerCarouselTranslationModelAdmin)

admin.site.register(BeerContainer, BeerContainerAdmin)
