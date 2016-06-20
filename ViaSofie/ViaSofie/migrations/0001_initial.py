# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actief', models.BooleanField(default=True)),
                ('titel', models.CharField(max_length=255)),
                ('titel_nl', models.CharField(max_length=255, null=True)),
                ('titel_en', models.CharField(max_length=255, null=True)),
                ('titel_fr', models.CharField(max_length=255, null=True)),
                ('tekst', models.TextField()),
                ('tekst_nl', models.TextField(null=True)),
                ('tekst_en', models.TextField(null=True)),
                ('tekst_fr', models.TextField(null=True)),
                ('prioriteit', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'FAQ item',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actief', models.BooleanField(default=True)),
                ('naam', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('logo', models.ImageField(upload_to='partner-img')),
                ('prioriteit', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
