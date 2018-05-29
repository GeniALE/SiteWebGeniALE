from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
from sponsorsModule import local_settings


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    def __str__(self):
        return self.name

class CategoryTranslation(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(Category)
    def __str__(self):
        return self.name

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

    # translations = models.ForeignKey(TeamDisplayTranslationModel, null=True)

    class Meta:
        verbose_name = "SponsorsModule Sponsors Display"
        verbose_name_plural = "SponsorsModule Sponsors Displays"
