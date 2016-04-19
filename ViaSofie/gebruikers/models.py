from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Gebruiker(models.Model):
    naam = models.CharField(max_length=255)
    voornaam = models.CharField(max_length=255)
    telefoonnummer = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    wachtwoord = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE)


class Adres(models.Model):
    straat = models.CharField(max_length=255)
    huisnummer = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    gemeente = models.CharField(max_length=255)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)


class Land(models.Model):
    naam = models.CharField(max_length=255)
    landcode = models.CharField(max_length=2)


class Rol(models.Model):
    naam = models.CharField(max_length=255)
    permissies = models.ManyToManyField(Permissie)


class Permissie(models.Model):
    label = models.CharField(max_length=10, unique=True)
