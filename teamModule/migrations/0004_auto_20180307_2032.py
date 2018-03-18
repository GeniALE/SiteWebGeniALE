# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 01:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0003_teamdisplay'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDisplayView',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='teammodule_teamdisplayview', serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(choices=[('teamModule/team_display.html', 'team_display.html')], default='teamModule/team_display.html', editable=False, max_length=255)),
                ('css_class_prefix', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'TeamModule Team Display',
                'verbose_name_plural': 'TeamModule Team Displays',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='teamdisplay',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='TeamDisplay',
        ),
    ]
