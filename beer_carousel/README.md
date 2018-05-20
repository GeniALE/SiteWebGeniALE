# beer_carousel

Beer carousel is a plugin that act as a carousel for your beers. 

You can add your beers in the admin panel and then add the plugin inside one of your page.

# Template configuration

To customize the template, simply copy paste the default template into your website.
In your `settings.py`, add the following entry:

```python

BEER_CAROUSEL_TEMPLATES_TEMPLATES = [
    ('beer_carousel/default.html', 'Default'),
    ('components/custom.html', 'Custom'),
];
```

You must have atleast two templates to be able to change it in the UI.