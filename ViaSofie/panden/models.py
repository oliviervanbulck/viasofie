from __future__ import unicode_literals

from django.db import models
from gebruikers.models import Gebruiker
from gebruikers.models import Adres


# Create your models here.

class Type(models.Model):
    type = models.CharField(max_length=255)


class Pand(models.Model):
    prijs = models.FloatField()
    bouwjaar = models.DateField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    gebruiker = models.ForeignKey(Gebruiker, on_delete=models.CASCADE)
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE)


class PandImmoLink(models.Model):
    site_beschrijving = models.CharField(max_length=255)
    site_link = models.CharField(max_length=255)
    pand = models.ForeignKey(Pand, on_delete=models.CASCADE)


class Foto(models.Model):
    foto_link = models.CharField(max_length=255)
    pand = models.ForeignKey(Pand, on_delete=models.CASCADE)


class Kenmerk(models.Model):
    benaming = models.CharField(max_length=50)


class PandKenmerkPerPand(models.Model):
    class Meta:
        unique_together = (('pand', 'kenmerk'),)
    aantal = models.PositiveSmallIntegerField()
    pand = models.ForeignKey(Pand, on_delete=models.CASCADE)
    kenmerk = models.ForeignKey(Kenmerk, on_delete=models.CASCADE)