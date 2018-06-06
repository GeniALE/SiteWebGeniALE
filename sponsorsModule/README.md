# SponsorsModule

SponsorsModule is a plugin that let you manage your sponsors.

One plugin is available to display all of your sponsors by range of donations.

The plugins's template can be customized.

# Sponsors display

By default, the following variables are injected with:

- Sponsors: An array of sponsors objects
- Categories: An array of categories objects

To customize the template, simply copy paste the default template into your website.

# Template configuration

In your `settings.py`, add the following entry:

```python

SPONSORSMODULE_SPONSORSDISPLAY_TEMPLATES = [
    ('sponsorsModule/sponsors_display.html', 'Default'),
    ('components/sponsors_display.html', 'Sponsors Display')
];

```

You must have atleast one template available in your components to be able to change it in the UI.