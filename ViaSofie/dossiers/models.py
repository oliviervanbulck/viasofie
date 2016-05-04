# Models voor dossiers gebaseerd op het ERD

from __future__ import unicode_literals

import datetime
import os

from django.db import models


# ERD tabel Dossier
from django.dispatch import receiver

from panden.models import Pand


class Dossier(models.Model):
    class Meta:
        verbose_name_plural = "Dossiers"
    actief = models.BooleanField(default=True)
    pand = models.OneToOneField('panden.Pand', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Dossier: ' + str(self.pand)


# ERD tabel StavazaLijnen
class StavazaLijn(models.Model):
    class Meta:
        verbose_name_plural = "Stavazalijnen"
    datum = models.DateField(default=datetime.date.today)
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
    dossier = models.ForeignKey('Dossier', on_delete=models.CASCADE)
    status = models.OneToOneField('DossierDocStatus', on_delete=models.CASCADE, null=True)
    beschrijving = models.OneToOneField('DossierDocBeschrijving', on_delete=models.CASCADE, null=True)
    beschrijving.verbose_name = 'Document'
    bestand = models.FileField(null=True, blank=True)

    def __str__(self):
        return '%s: %s (%s)' % (str(self.dossier), str(self.beschrijving), str(self.status))


@receiver(models.signals.post_delete, sender=DossierDocLijn)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.foto:
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)


@receiver(models.signals.pre_save, sender=DossierDocLijn)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = DossierDocLijn.objects.get(pk=instance.pk).bestand
    except DossierDocLijn.DoesNotExist:
        return False

    new_file = instance.bestand
    if not old_file.name:
        return False
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


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
        return self.dossier_naam.naam
