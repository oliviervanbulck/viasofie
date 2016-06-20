# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gebruikers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselFoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to=b'')),
                ('actief', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'foto voor slideshow',
                'verbose_name_plural': 'slideshow',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'verbose_name_plural': "foto's",
            },
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ImmoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_beschrijving', models.CharField(max_length=255, verbose_name='beschrijving')),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Kenmerk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benaming', models.CharField(max_length=50)),
                ('benaming_nl', models.CharField(max_length=50, null=True)),
                ('benaming_en', models.CharField(max_length=50, null=True)),
                ('benaming_fr', models.CharField(max_length=50, null=True)),
                ('is_aantal', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'kenmerken',
            },
        ),
        migrations.CreateModel(
            name='KenmerkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prijs', models.FloatField()),
                ('bouwjaar', models.PositiveSmallIntegerField()),
                ('oppervlakte', models.FloatField()),
                ('algemene_beschrijving', models.TextField()),
                ('algemene_beschrijving_nl', models.TextField(null=True)),
                ('algemene_beschrijving_en', models.TextField(null=True)),
                ('algemene_beschrijving_fr', models.TextField(null=True)),
                ('actief', models.BooleanField(default=True)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcode')),
                ('adres', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gebruikers.Adres')),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gebruikers.Gebruiker')),
            ],
            options={
                'verbose_name_plural': 'panden',
            },
        ),
        migrations.CreateModel(
            name='PandImmoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_link', models.CharField(max_length=255, verbose_name='link')),
                ('pand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Pand')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.ImmoSite')),
            ],
            options={
                'verbose_name_plural': 'immolinks',
            },
        ),
        migrations.CreateModel(
            name='PandKenmerkPerPand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aantal', models.PositiveSmallIntegerField()),
                ('kenmerk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Kenmerk')),
                ('pand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Pand')),
            ],
            options={
                'verbose_name': 'pandkenmerk',
                'verbose_name_plural': 'pandkenmerken',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=20)),
                ('waarde', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'optie',
                'verbose_name_plural': 'opties',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('type_nl', models.CharField(max_length=255, null=True)),
                ('type_en', models.CharField(max_length=255, null=True)),
                ('type_fr', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'types',
            },
        ),
        migrations.AddField(
            model_name='pand',
            name='kenmerken',
            field=models.ManyToManyField(through='panden.PandKenmerkPerPand', to='panden.Kenmerk'),
        ),
        migrations.AddField(
            model_name='pand',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Type'),
        ),
        migrations.AddField(
            model_name='kenmerk',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panden.KenmerkType'),
        ),
        migrations.AddField(
            model_name='hit',
            name='pand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Pand'),
        ),
        migrations.AddField(
            model_name='foto',
            name='pand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panden.Pand'),
        ),
        migrations.AlterUniqueTogether(
            name='pandkenmerkperpand',
            unique_together=set([('pand', 'kenmerk')]),
        ),
    ]
