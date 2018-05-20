from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import BeerModel, BeerCarouselPluginModel


@plugin_pool.register_plugin
class BeerCarouselPlugin(CMSPluginBase):
    name = _("Beer carousel plugin")
    model = BeerCarouselPluginModel
    render_template = "beer_carousel/default.html"
    cache = False

    def get_beers(self):
        return BeerModel.objects.all()

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        context = super(BeerCarouselPlugin, self).render(context, instance, placeholder)
        beers = self.get_beers()

        context.update({
            'beers': beers,
            'uniqueName': 'beerCarousel' + '__' + str(instance.id),
            'translations': instance.translations
        })
        return context
