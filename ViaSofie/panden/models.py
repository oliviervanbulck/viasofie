# Models voor panden gebaseerd op het ERD

from __future__ import unicode_literals

from django.contrib import admin
from django.db import models


# Create your models here.

# ERD tabel Type
from django.utils.encoding import python_2_unicode_compatible


class Type(models.Model):
    class Meta:
        verbose_name_plural = "Types"
    type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.type)


# ERD tabel Kenmerk
class Kenmerk(models.Model):
    class Meta:
        verbose_name_plural = "Kenmerken"
    benaming = models.CharField(max_length=50)

    def __str__(self):
        return str(self.benaming)


@python_2_unicode_compatible
# ERD tabel Pand
class Pand(models.Model):
    class Meta:
        verbose_name_plural = "Panden"
    prijs = models.FloatField()
    bouwjaar = models.DateField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    gebruiker = models.ForeignKey('gebruikers.Gebruiker', on_delete=models.CASCADE)
    adres = models.OneToOneField('gebruikers.Adres', on_delete=models.CASCADE, null=True)
    kenmerken = models.ManyToManyField('Kenmerk', through='PandKenmerkPerPand')
    dossier = models.OneToOneField('dossiers.Dossier', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.type) + ' - ' + str(self.adres)


# ERD tabel PandImmoLink
class PandImmoLink(models.Model):
    class Meta:
        verbose_name_plural = "Immolinks"
    site_beschrijving = models.CharField(max_length=255)
    site_link = models.CharField(max_length=255)
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.site_beschrijving) + ' - ' + str(self.pand)


# ERD tabel Foto
class Foto(models.Model):
    class Meta:
        verbose_name_plural = "Foto's"
    foto = models.ImageField(null=True)
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)

    def __str__(self):
        return self.foto.url

    def get_admin_url(self):
        return "/admin/panden/foto/%d/" % self.id


# ERD tabel PandKenmerkPerPand
class PandKenmerkPerPand(models.Model):
    class Meta:
        unique_together = (('pand', 'kenmerk'),)
        verbose_name_plural = "Kenmerken per pand"
    aantal = models.PositiveSmallIntegerField()
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)
    kenmerk = models.ForeignKey('Kenmerk', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kenmerk) + ' - ' + str(self.aantal) + ' - ' + str(self.pand)