# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panden', '0025_auto_20160609_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='pand',
            name='algemene_beschrijving_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pand',
            name='algemene_beschrijving_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pand',
            name='algemene_beschrijving_nl',
            field=models.TextField(null=True),
        ),
    ]
