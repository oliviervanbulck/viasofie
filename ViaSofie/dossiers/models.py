from __future__ import unicode_literals

from django.db import models


class Dossier(models.Model):
    class Meta:
        verbose_name_plural = "Dossiers"
    actief = models.BooleanField
    pand = models.ForeignKey('panden.Pand', on_delete=models.CASCADE)

    def __str__(self):
        return 'Dossier: ' + str(self.pand)


class StavazaLijn(models.Model):
    class Meta:
        verbose_name_plural = "Stavazalijnen"
    datum = models.DateField
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    stavaza = models.OneToOneField('Stavaza', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.dossier.pand) + str(self.stavaza.status)


class Stavaza(models.Model):
    class Meta:
        verbose_name_plural = "Stavaza's"
    status = models.CharField(max_length=255)

    def __str__(self):
        return str(self.status)


class DossierDocLijn(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Lijnen"
    link = models.CharField(max_length=255)
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    status = models.OneToOneField('DossierDocStatus', on_delete=models.CASCADE, null=True)
    beschrijving = models.OneToOneField('DossierDocBeschrijving', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s: %s (%s)' % (str(self.dossier), str(self.beschrijving), str(self.status))


class DossierDocStatus(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Statussen"
    status = models.IntegerField

    def __str__(self):
        return str(self.status)


class DossierDocBeschrijving(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Beschrijvingen"
    dossier_naam = models.CharField(max_length=255)
    kan_doc_bevatten = models.SmallIntegerField

    def __str__(self):
        return str(self.dossier_naam)
