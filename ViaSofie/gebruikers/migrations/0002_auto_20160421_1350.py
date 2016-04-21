# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gebruikers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gebruiker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='gebruiker',
            name='naam',
        ),
        migrations.RemoveField(
            model_name='gebruiker',
            name='rol',
        ),
        migrations.RemoveField(
            model_name='gebruiker',
            name='voornaam',
        ),
        migrations.RemoveField(
            model_name='gebruiker',
            name='wachtwoord',
        ),
        migrations.AddField(
            model_name='gebruiker',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
