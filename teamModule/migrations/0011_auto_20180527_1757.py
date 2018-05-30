# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0010_auto_20180411_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDisplayTranslationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'ProjectDisplay Translation model',
                'verbose_name_plural': 'ProjectDisplay Translation models',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDisplayTranslationModelTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_title', models.CharField(default='Our Projects', max_length=255)),
                ('project_title', models.CharField(default='Project Title', max_length=255)),
                ('project_description_title', models.CharField(default='Project Title', max_length=255)),
                ('project_status_title', models.CharField(default='Status', max_length=255)),
                ('project_website_title', models.CharField(default='Website', max_length=255)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='teamModule.ProjectDisplayTranslationModel')),
            ],
            options={
                'db_table': 'teamModule_projectdisplaytranslationmodel_translation',
                'default_permissions': (),
                'managed': True,
                'abstract': False,
                'db_tablespace': '',
            },
        ),
        migrations.AddField(
            model_name='projectdisplayview',
            name='translations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teamModule.ProjectDisplayTranslationModel'),
        ),
        migrations.AlterUniqueTogether(
            name='projectdisplaytranslationmodeltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
