# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        #('cms', '0019_auto_20180411_2100'),
        ('teamModule', '0009_auto_20180410_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDisplayView',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='teammodule_projectdisplayview', serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(choices=[('teamModule/project_display.html', 'List projects')], default='projectModule/project_display.html', editable=False, max_length=255)),
                ('css_class_prefix', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'verbose_name': 'TeamModule Project Display',
                'verbose_name_plural': 'TeamModule Project Displays',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='teamModule.Project'),
        ),
    ]
