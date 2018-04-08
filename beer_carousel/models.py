from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields

# Plugins models
from beer_carousel import local_settings


class BeerTranslationsModel(TranslatableModel):
    translations = TranslatedFields(
        description=models.CharField(max_length=255, null=True, blank=True),
    )


class BeerModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    alcohol_percent = models.IntegerField(blank=False)
    ibu = models.IntegerField(blank=False)
    image = models.ImageField()
    type = models.CharField(max_length=100, blank=False)
    service_temperature = models.CharField(max_length=10, blank=True)
    created_at = models.DateField(blank=True)

    translations = models.ForeignKey(BeerTranslationsModel, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BeerCarouselPluginTranslationModel(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, default="Beers"),
        creation_date=models.CharField(max_length=255, default="Created"),
        type=models.CharField(max_length=255, default="Type"),
        alcohol_percent=models.CharField(max_length=255, default="Alcohol %"),
        service_temperature=models.CharField(max_length=255, default="Service temperature"),
        ibu=models.CharField(max_length=255, default="IBU"),
    )

    class Meta:
        verbose_name = "Beer carousel's translations"
        verbose_name_plural = "Beer carousel' translations"


@python_2_unicode_compatible
class BeerCarouselPluginModel(CMSPlugin):
    template = models.CharField(
        max_length=255,
        choices=local_settings.BEER_CAROUSEL_TEMPLATES_TEMPLATES,
        default='beer_carousel/default.html',
        editable=len(local_settings.BEER_CAROUSEL_TEMPLATES_TEMPLATES) > 1)

    translations = models.ForeignKey(BeerCarouselPluginTranslationModel, null=True)

    class Meta:
        verbose_name = "Beer carousel plugin"
        verbose_name_plural = "Beer carousel plugins"
