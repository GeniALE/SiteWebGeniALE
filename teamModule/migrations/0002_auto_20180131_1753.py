# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.CharField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedInUrl',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profilePicUrl',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
