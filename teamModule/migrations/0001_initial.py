# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('bio', models.CharField(max_length=400, blank=True)),
                ('email', models.CharField(max_length=75)),
                ('linkedInUrl', models.CharField(max_length=200, blank=True)),
                ('profilePicUrl', models.CharField(max_length=200, blank=True)),
                ('formation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teamModule.Formation')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'project statuses',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('team', models.ForeignKey(to='teamModule.Team')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='teamModule.ProjectStatus'),
        ),
        migrations.AddField(
            model_name='member',
            name='projects',
            field=models.ManyToManyField(to='teamModule.Project'),
        ),
        migrations.AddField(
            model_name='member',
            name='teamRoles',
            field=models.ManyToManyField(to='teamModule.TeamRole'),
        ),
    ]
