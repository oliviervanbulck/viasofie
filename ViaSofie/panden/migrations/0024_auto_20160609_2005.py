# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panden', '0023_auto_20160606_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='kenmerk',
            name='benaming_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kenmerk',
            name='benaming_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kenmerk',
            name='benaming_nl',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
