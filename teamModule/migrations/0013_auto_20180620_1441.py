# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0012_merge_20180620_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
    ]