# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikers', '0004_auto_20160422_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gebruiker',
            name='adres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gebruikers.Adres'),
        ),
    ]
