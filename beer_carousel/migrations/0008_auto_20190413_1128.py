# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-13 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
  dependencies = [
    ('beer_carousel', '0007_auto_20180616_1259'),
  ]

  operations = [
    migrations.RenameField(
      model_name='beermodel',
      old_name='image_scale',
      new_name='image_scale_x',
    ),
    migrations.AddField(
      model_name='beermodel',
      name='image_scale_y',
      field=models.FloatField(default=3),
    ),
  ]
