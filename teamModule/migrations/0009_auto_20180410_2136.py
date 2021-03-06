# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
  dependencies = [
    ('teamModule', '0008_merge_20180408_1202'),
  ]

  operations = [
    migrations.CreateModel(
      name='TeamDisplayTranslationModel',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      ],
      options={
        'verbose_name': 'TeamDisplay Translation model',
        'verbose_name_plural': 'TeamDisplay Translation models',
      },
      managers=[
        ('objects', django.db.models.manager.Manager()),
        ('_plain_manager', django.db.models.manager.Manager()),
      ],
    ),
    migrations.CreateModel(
      name='TeamDisplayTranslationModelTranslation',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('teams_title', models.CharField(default='Teams', max_length=255)),
        ('all', models.CharField(default='All', max_length=255)),
        ('members_title', models.CharField(default='Members', max_length=255)),
        ('projects_title', models.CharField(default='Projects', max_length=255)),
        ('formation_title', models.CharField(default='Formation', max_length=255)),
        ('language_code', models.CharField(db_index=True, max_length=15)),
        ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                     related_name='translations', to='teamModule.TeamDisplayTranslationModel')),
      ],
      options={
        'managed': True,
        'db_table': 'teamModule_teamdisplaytranslationmodel_translation',
        'abstract': False,
        'default_permissions': (),
        'db_tablespace': '',
      },
    ),
    migrations.AlterModelOptions(
      name='teambannertranslationmodel',
      options={'verbose_name': 'TeamBanner Translation model',
               'verbose_name_plural': 'TeamBanner Translation models'},
    ),
    migrations.RemoveField(
      model_name='teamdisplayview',
      name='select_all_text',
    ),
    migrations.AlterField(
      model_name='projectstatus',
      name='status',
      field=models.CharField(max_length=20),
    ),
    migrations.AlterField(
      model_name='team',
      name='team_name',
      field=models.CharField(max_length=100),
    ),
    migrations.AlterField(
      model_name='teambannermodel',
      name='template',
      field=models.CharField(choices=[('teamModule/member_banner.html', 'Default'),
                                      ('components/member_banner.html', 'Team banner')],
                             default='teamModule/member_banner.html', max_length=255),
    ),
    migrations.AlterField(
      model_name='teambannertranslationmodeltranslation',
      name='member_more_detail',
      field=models.CharField(default='More details', max_length=255),
    ),
    migrations.AlterField(
      model_name='teambannertranslationmodeltranslation',
      name='members',
      field=models.CharField(default='members', max_length=255),
    ),
    migrations.AlterField(
      model_name='teamdisplayview',
      name='template',
      field=models.CharField(choices=[('teamModule/team_display.html', 'Default'),
                                      ('components/member_count.html', 'Total member count'),
                                      ('components/team_display.html', 'Team member display')],
                             default='teamModule/team_display.html', max_length=255),
    ),
    migrations.AlterField(
      model_name='teamrole',
      name='role',
      field=models.CharField(max_length=100),
    ),
    migrations.AddField(
      model_name='teamdisplayview',
      name='translations',
      field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                              to='teamModule.TeamDisplayTranslationModel'),
    ),
    migrations.AlterUniqueTogether(
      name='teamdisplaytranslationmodeltranslation',
      unique_together=set([('language_code', 'master')]),
    ),
  ]
