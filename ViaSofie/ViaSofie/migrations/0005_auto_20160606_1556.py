# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ViaSofie', '0004_faqitem_actief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='actief',
            field=models.BooleanField(default=True),
        ),
    ]
