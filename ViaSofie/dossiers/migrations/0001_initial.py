# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('panden', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Pand')),
            ],
        ),
        migrations.CreateModel(
            name='DossierDocBeschrijving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dossier_naam', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DossierDocLijn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('dossier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dossiers.Dossier')),
            ],
        ),
        migrations.CreateModel(
            name='DossierDocStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dossier_doc_lijn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dossiers.DossierDocLijn')),
            ],
        ),
        migrations.CreateModel(
            name='Stavaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StavazaLijn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dossier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dossiers.Dossier')),
            ],
        ),
        migrations.AddField(
            model_name='stavaza',
            name='stavaza_lijn_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dossiers.StavazaLijn'),
        ),
        migrations.AddField(
            model_name='dossierdocbeschrijving',
            name='dossier_doc_lijn_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dossiers.DossierDocLijn'),
        ),
    ]