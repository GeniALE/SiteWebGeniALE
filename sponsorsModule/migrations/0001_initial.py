# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Category',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=100)),
        ('scoreMin', models.IntegerField()),
        ('scoreMax', models.IntegerField()),
      ],
    ),
    migrations.CreateModel(
      name='CategoryTranslation',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=100)),
      ],
    ),
    migrations.CreateModel(
      name='Sponsor',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('title', models.CharField(max_length=100)),
        ('url', models.URLField()),
        ('image', models.ImageField(upload_to='media/')),
      ],
    ),
    migrations.CreateModel(
      name='SponsorsDisplayView',
      fields=[
        ('cmsplugin_ptr',
         models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                              primary_key=True, related_name='sponsorsmodule_sponsorsdisplayview',
                              serialize=False, to='cms.CMSPlugin')),
        ('template', models.CharField(choices=[('sponsorsModule/sponsors_display.html', 'Default'),
                                               ('components/sponsors_display.html', 'Sponsors Display')],
                                      default='sponsorsModule/sponsorsmodule_display.html', max_length=255)),
        ('css_class_prefix', models.CharField(blank=True, default='', max_length=100)),
      ],
      options={
        'verbose_name': 'SponsorsModule Sponsors Display',
        'verbose_name_plural': 'SponsorsModule Sponsors Displays',
      },
      bases=('cms.cmsplugin',),
    ),
  ]
