# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='url',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='description',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
    ]
