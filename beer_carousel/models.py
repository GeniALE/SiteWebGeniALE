from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields

# Plugins models
from beer_carousel import local_settings


class BeerTranslationsModel(TranslatableModel):
    translations = TranslatedFields(
        description=models.TextField(null=True, blank=True),
    )

    def __str__(self):
        return "Beer's translations ({})".format(self.id)


class BeerModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    alcohol_percent = models.FloatField(blank=False)
    ibu = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='media/')
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
        alcohol_percent=models.CharField(max_length=255, default="Alcohol percentage"),
        service_temperature=models.CharField(max_length=255, default="Service temperature"),
        ibu=models.CharField(max_length=255, default="IBU"),
    )

    def __str__(self):
        return "Beer carousel's translations({})".format(self.id)

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

    translations = models.ForeignKey(BeerCarouselPluginTranslationModel)

    class Meta:
        verbose_name = "Beer carousel plugin"
        verbose_name_plural = "Beer carousel plugins"
