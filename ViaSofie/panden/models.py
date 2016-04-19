from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pand(models.Model):
    prijs = models.FloatField()
    bouwjaar = models.DateField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.CharField(1000)


class Type(models.Model):
    type = models.CharField(255)


class Foto(models.Model):
    foto_link = models.CharField()
