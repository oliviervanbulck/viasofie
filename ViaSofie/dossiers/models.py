from __future__ import unicode_literals

from django.db import models

from panden.models import Pand


class Dossier(models.Model):
    actief = models.BooleanField
    pand_id = models.ForeignKey(Pand, on_delete=models.CASCADE)


class StavazaLijn(models.Model):
    datum = models.DateField
    dossier_id = models.ForeignKey(Dossier, on_delete=models.CASCADE)


class Stavaza(models.Model):
    status = models.CharField(max_length=255)
    stavaza_lijn_id = models.ForeignKey(StavazaLijn, on_delete=models.CASCADE)


class DossierDocLijn(models.Model):
    link = models.CharField(max_length=255)
    dossier_id = models.ForeignKey(Dossier, on_delete=models.CASCADE)


class DossierDocStatus(models.Model):
    status = models.IntegerField
    dossier_doc_lijn_id = models.ForeignKey(DossierDocLijn, on_delete=models.CASCADE)


class DossierDocBeschrijving(models.Model):
    dossier_naam = models.CharField(max_length=255)
    kan_doc_bevatten = models.SmallIntegerField
    dossier_doc_lijn_id = models.ForeignKey(DossierDocLijn, on_delete=models.CASCADE)