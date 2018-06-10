# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beercarouselpluginmodel',
            name='template',
            field=models.CharField(choices=[('beer_carousel/default.html', 'Default'), ('components/beer_carousel.html', 'Custom beer template')], default='beer_carousel/default.html', max_length=255),
        ),
        migrations.AlterField(
            model_name='beercarouselplugintranslationmodeltranslation',
            name='alcohol_percent',
            field=models.CharField(default='Alcohol percentage', max_length=255),
        ),
        migrations.AlterField(
            model_name='beermodel',
            name='alcohol_percent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='beermodel',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='beertranslationsmodeltranslation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]