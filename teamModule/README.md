# Custom templates

This plugin allow you to define your own templates.
Templates are highly customizable.

By default, they are injected with:

- members: An array of members objects
- teams: An array of teams objects
- idSuffix: A suffix for all your id. This is used to use the same plugin twice on the same page.
- cssPrefix: A CSS prefix for all your CSS classes. This is ideal to customize the actual CSS.

## Configuration

In your `settings.py`, add the following entry:

```python

TEAMMODULE_TEAMDISPLAY_TEMPLATES = [
    ('teamModule/team_display.html', 'team_display.html'),
    ('my_custom_template.html', 'Team banner')
]
```

You must have atleast two templates to  be able to change it in the UI.