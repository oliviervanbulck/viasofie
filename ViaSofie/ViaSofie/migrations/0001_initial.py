# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faq_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('tekst', models.TextField()),
            ],
            options={
                'verbose_name': 'FAQ item',
            },
        ),
    ]