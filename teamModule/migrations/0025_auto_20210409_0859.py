# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-04-09 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0024_auto_20210324_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='honorable_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='teamdisplayview',
            name='template',
            field=models.CharField(choices=[('teamModule/team_display.html', 'Default'), ('components/member_count.html', 'Total member count'), ('components/team_display.html', 'Team member display'), ('components/honorable_members_display.html', 'Honorable member display')], default='teamModule/team_display.html', max_length=255),
        ),
    ]
