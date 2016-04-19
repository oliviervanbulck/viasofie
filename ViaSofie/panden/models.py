from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Pand(models.Model):
    prijs = models.FloatField()
    bouwjaar = models.DateField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.TextField()


class Type(models.Model):
    type = models.CharField(max_length=255)


class Foto(models.Model):
    foto_link = models.CharField(max_length=255)


class PandKenmerkPerPand(models.Model):
    aantal = models.PositiveSmallIntegerField()


class Kenmerk(models.Model):
    benaming = models.CharField(max_length=50)


class PandImmoLink(models.Model):
    site_beschrijving = models.CharField(max_length=255)
    site_link = models.CharField(max_length=255)
