# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossiers', '0007_dossier_pand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossierdoclijn',
            name='link',
        ),
        migrations.AddField(
            model_name='dossierdoclijn',
            name='bestand',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
