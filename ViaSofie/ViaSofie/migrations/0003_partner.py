# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViaSofie', '0002_auto_20160606_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actief', models.BooleanField()),
                ('naam', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
