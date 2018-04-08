from django.conf import settings

BEER_CAROUSEL_TEMPLATES_TEMPLATES = getattr(settings, 'BEER_CAROUSEL_TEMPLATES_TEMPLATES', [
    ('beer_carousel/default.html', 'Default'),
])