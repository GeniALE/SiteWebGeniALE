# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
  dependencies = [
    ('beer_carousel', '0006_auto_20180610_1414'),
  ]

  operations = [
    migrations.AddField(
      model_name='beercarouselplugintranslationmodeltranslation',
      name='back_label',
      field=models.CharField(default='Back', max_length=255),
    ),
    migrations.AddField(
      model_name='beercarouselplugintranslationmodeltranslation',
      name='next_label',
      field=models.CharField(default='Next', max_length=255),
    ),
  ]
