# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0012_auto_20160521_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossierdocbeschrijving',
            name='dossier_naam',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dossierdocstatus',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stavaza',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]