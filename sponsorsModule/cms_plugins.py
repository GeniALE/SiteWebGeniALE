from collections import OrderedDict

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.forms import model_to_dict
from django.utils.translation import ugettext_lazy as _
import json

from sponsorsModule.helpers import to_dict
from .models import CategoryTranslation, Category, Sponsor, SponsorsDisplayView


@plugin_pool.register_plugin
class SponsorsModulePlugin(CMSPluginBase):
    name = _("Sponsors display plugin")
    model = SponsorsDisplayView
    render_template = "sponsorsModule/sponsors_display.html"
    cache = False

    def get_sponsors(self):
        sponsors = list(Sponsor.objects.all().order_by("title"))
        return sponsors

    def get_categories(self, instance):
        categories = list(Category.objects.all().order_by("-scoreMin"))
        return categories

    def add_category_to_sponsor(self, sponsors, category):
        for sponsor in sponsors:
            sponsor.category = []
            for c in category:
                if c.scoreMax is not None:
                    if c.scoreMin <= sponsor.score <= c.scoreMax:
                        sponsor.category.append(c)
                else:
                    if sponsor.score >= c.scoreMin:
                        sponsor.category.append(c)
        return sponsors

    def add_sponsors_to_categories(self, sponsors, category):
        # sortedcategories = sorted(category,key = lambda x: x.scoreMin)

        for c in category:
            c.sponsors = []
            for sponsor in sponsors:
                if c.scoreMax is not None:
                    if c.scoreMin <= sponsor.score <= c.scoreMax:
                        c.sponsors.append(sponsor)
                else:
                    if sponsor.score >= c.scoreMin:
                        c.sponsors.append(sponsor)
        return category

    def get_image_url(self, sponsors):
        for sponsor in sponsors:
            sponsor.image = "/media/" + str(sponsor.image)
        return sponsors

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(SponsorsModulePlugin, self).render(context, instance, placeholder)

        # Get some data
        sponsors = self.get_sponsors()
        sponsors = self.get_image_url(sponsors)
        categories = self.get_categories(instance)
        # sponsors_category = self.add_category_to_sponsor(sponsors, categories)
        category_sponsors = self.add_sponsors_to_categories(sponsors, categories)
        context.update({
            'sponsors': sponsors,
            'categories': categories,
            'category_sponsors': category_sponsors,
            'cssPrefix': instance.css_class_prefix
        })
        return context