# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panden', '0020_pandimmolink_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImmoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_beschrijving', models.CharField(max_length=255, verbose_name='beschrijving')),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='pandimmolink',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='pandimmolink',
            name='site_beschrijving',
        ),
    ]