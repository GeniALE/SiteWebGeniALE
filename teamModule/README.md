# TeamModule

- [TeamModule](#teammodule)
- [Team display](#team-display)
- [Team banner](#team-banner)
- [Template configuration](#template-configuration)

TeamModule is a plugin that let you manage your team and your projects.

Some plugins are available to display:

- Your members (team_display)
- Your team (team_banner)

Each plugins's template can be customize.

# Team display

By default, the following variables are injected with:

- members: An array of members objects
- teams: An array of teams objects
- cssPrefix: A CSS prefix for all your CSS classes. This is ideal to customize the actual CSS.

To customize the template, simply copy paste the default template into your website.

# Team banner

For this plugin, you'll have to configure:

- A team image
- Some translations (member, member description, team description, button text)

The member count displayed will be fetch from the database.

To customize the template, simply copy paste the default template into your website.

# Template configuration

In your `settings.py`, add the following entry:

```python

TEAMMODULE_TEAMDISPLAY_TEMPLATES = [
    ('teamModule/team_display.html', 'team_display.html'),
    ('my_custom_template.html', 'Team banner')
];

TEAMMODULE_TEAMBANNER_TEMPLATES = [
    ('teamModule/member_banner.html', 'Default'),
    ('my_custom_template.html','Custom banner')
];
```

You must have atleast two templates to be able to change it in the UI.