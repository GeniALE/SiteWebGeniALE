from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
from sponsorsModule import local_settings


class CategoryTranslation(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
    )

    def __str__(self):
        return str(self.lazy_translation_getter('name', self.pk))

    class Meta:
        verbose_name = "Category Translation model"
        verbose_name_plural = "Categories Translation models"


class Category(models.Model):
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    translation = models.ForeignKey(CategoryTranslation, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.translation)


class Sponsor(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='media/')
    score = models.IntegerField()

    def __str__(self):
        return self.title


"""
Plugins models
"""


class SponsorsDisplayViewTranslations(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=False)
    )

    class Meta:
        verbose_name = "Sponsors plugin translation"
        verbose_name_plural = "Sponsor plugin translations"

    def __str__(self):
        return str(self.lazy_translation_getter('title', self.pk))


@python_2_unicode_compatible
class SponsorsDisplayView(CMSPlugin):
    template = models.CharField(
        max_length=255,
        choices=local_settings.SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES,
        default='sponsorsModule/sponsorsmodule_display.html',
        editable=len(local_settings.SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES) > 1)
    css_class_prefix = models.CharField(
        max_length=100,
        default="",
        blank=True
    )
    translation = models.ForeignKey(SponsorsDisplayViewTranslations, null=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "SponsorsModule Sponsors Display"
        verbose_name_plural = "SponsorsModule Sponsors Displays"
