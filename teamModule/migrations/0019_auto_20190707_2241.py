# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-08 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0018_auto_20190503_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membertranslation',
            name='bio',
            field=models.CharField(blank=True, max_length=1200),
        ),
    ]
