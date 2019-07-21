# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
  dependencies = [
    ('teamModule', '0002_auto_20180201_1518'),
  ]

  operations = [
    migrations.CreateModel(
      name='TeamDisplay',
      fields=[
        ('cmsplugin_ptr',
         models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                              primary_key=True, related_name='teammodule_teamdisplay', serialize=False,
                              to='cms.CMSPlugin')),
      ],
      options={
        'abstract': False,
      },
      bases=('cms.cmsplugin',),
    ),
  ]
