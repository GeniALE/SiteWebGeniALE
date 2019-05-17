# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-04 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0017_auto_20190428_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='member',
            name='date_left',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]