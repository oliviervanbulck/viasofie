from __future__ import unicode_literals

from django.db import models


class Dossier(models.Model):
    class Meta:
        verbose_name_plural = "Dossiers"
    actief = models.BooleanField
    pand = models.ForeignKey('panden.Pand', on_delete=models.CASCADE)


class StavazaLijn(models.Model):
    class Meta:
        verbose_name_plural = "Stavazalijnen"
    datum = models.DateField
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)


class Stavaza(models.Model):
    class Meta:
        verbose_name_plural = "Stavaza's"
    status = models.CharField(max_length=255)
    stavaza_lijn = models.ForeignKey('StavazaLijn', on_delete=models.CASCADE)


class DossierDocLijn(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Lijnen"
    link = models.CharField(max_length=255)
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)


class DossierDocStatus(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Statussen"
    status = models.IntegerField
    dossier_doc_lijn = models.ForeignKey('DossierDocLijn', on_delete=models.CASCADE)


class DossierDocBeschrijving(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Beschrijvingen"
    dossier_naam = models.CharField(max_length=255)
    kan_doc_bevatten = models.SmallIntegerField
    dossier_doc_lijn = models.ForeignKey('DossierDocLijn', on_delete=models.CASCADE)