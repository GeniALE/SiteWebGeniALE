# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-10-05 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceInstructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('register_url', models.CharField(blank=True, max_length=255, null=True)),
                ('unregister_url', models.CharField(blank=True, max_length=255, null=True)),
                ('member_mapping_to_username', models.CharField(max_length=50)),
                ('instruction_file', models.FileField(blank=True, upload_to='medias/')),
            ],
        ),
    ]
