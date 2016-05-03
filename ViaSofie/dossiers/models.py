# Models voor dossiers gebaseerd op het ERD

from __future__ import unicode_literals

from django.db import models


# ERD tabel Dossier
from panden.models import Pand


class Dossier(models.Model):
    class Meta:
        verbose_name_plural = "Dossiers"
    actief = models.BooleanField(default=True)
    pand = models.OneToOneField('panden.Pand', on_delete=models.CASCADE, null=True)

    def __str__(self):
        # pand = Pand.objects.filter(dossier_id=self.id)
        # return 'Dossier: ' + (str(pand.first()) if pand.count() == 1 else 'Nog niet gekoppeld aan een pand')
        return 'Dossier: ' + str(self.pand)


# ERD tabel StavazaLijnen
class StavazaLijn(models.Model):
    class Meta:
        verbose_name_plural = "Stavazalijnen"
    datum = models.DateField()
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    stavaza = models.OneToOneField('Stavaza', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.dossier.pand) + str(self.stavaza.status)


# ERD tabel Stavaza
class Stavaza(models.Model):
    class Meta:
        verbose_name_plural = "Stavaza's"
    status = models.ForeignKey('talen.Label', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)


# ERD tabel DossierDocLijnen
class DossierDocLijn(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Lijnen"
    link = models.CharField(max_length=255)
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    status = models.OneToOneField('DossierDocStatus', on_delete=models.CASCADE, null=True)
    beschrijving = models.OneToOneField('DossierDocBeschrijving', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s: %s (%s)' % (str(self.dossier), str(self.beschrijving), str(self.status))


# ERD tabel DossierDocStatus
class DossierDocStatus(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Statussen"
    status = models.ForeignKey('talen.Label', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status)


# ERD tabel DossierDocBeschrijving
class DossierDocBeschrijving(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Beschrijvingen"
    dossier_naam = models.ForeignKey('talen.Label', on_delete=models.CASCADE)
    kan_doc_bevatten = models.BooleanField(default=False)

    def __str__(self):
        return "Dossiernaam moet hier komen!"
