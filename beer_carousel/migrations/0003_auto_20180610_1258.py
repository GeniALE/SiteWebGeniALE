# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer_carousel', '0002_auto_20180605_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('css_class', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='beermodel',
            name='beer_container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer_carousel.BeerContainer'),
        ),
    ]
