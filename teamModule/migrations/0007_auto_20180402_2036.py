# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0006_merge_20180317_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamdisplayview',
            name='select_all_text',
            field=models.CharField(default='All', max_length=100),
        ),
        migrations.AlterField(
            model_name='teamdisplayview',
            name='template',
            field=models.CharField(choices=[('components/member_count.html', 'Total member count'), ('components/team_display.html', 'Team member display')], default='teamModule/team_display.html', max_length=255),
        ),
    ]