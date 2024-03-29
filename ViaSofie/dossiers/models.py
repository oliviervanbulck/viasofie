# Models voor dossiers gebaseerd op het ERD

from __future__ import unicode_literals

import datetime
import os

from django.db import models

# ERD tabel Dossier
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from panden.models import Pand


# ERD tabel StavazaLijnen
@python_2_unicode_compatible
class StavazaLijn(models.Model):
    class Meta:
        verbose_name_plural = "Stavazalijnen"

    datum = models.DateField(default=datetime.date.today)
    pand = models.ForeignKey('panden.Pand', on_delete=models.CASCADE)
    stavaza = models.ForeignKey('Stavaza', on_delete=models.CASCADE)
    stavaza.verbose_name = 'Actuele status'

    def __str__(self):
        return str(self.pand) + ' | ' + str(self.stavaza.status)


# ERD tabel Stavaza
@python_2_unicode_compatible
class Stavaza(models.Model):
    class Meta:
        verbose_name_plural = "Stavaza's"

    # status = models.ForeignKey('talen.Label', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


# ERD tabel DossierDocLijnen
@python_2_unicode_compatible
class DossierDocLijn(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Lijnen"
        unique_together = ('pand', 'beschrijving')

    pand = models.ForeignKey('panden.Pand', on_delete=models.CASCADE)
    beschrijving = models.ForeignKey('DossierDocBeschrijving', on_delete=models.CASCADE, null=True)
    beschrijving.verbose_name = 'Document'
    status = models.ForeignKey('DossierDocStatus', on_delete=models.CASCADE, null=True)
    bestand = models.FileField(null=True, blank=True)

    def __str__(self):
        return '%s | %s (%s)' % (self.pand, self.beschrijving, self.status)


# Automatisch verwijderen van document bestand na verwijderen
@receiver(models.signals.post_delete, sender=DossierDocLijn)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if kwargs.get('raw'):
        return
    if instance.bestand:
        if os.path.isfile(instance.bestand.path):
            os.remove(instance.bestand.path)


# Automatisch verwijderen van bestand bij wijzigen van document
@receiver(models.signals.pre_save, sender=DossierDocLijn)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if kwargs.get('raw'):
        return
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
@python_2_unicode_compatible
class DossierDocStatus(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Statussen"

    # status = models.ForeignKey('talen.Label', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


# ERD tabel DossierDocBeschrijving
@python_2_unicode_compatible
class DossierDocBeschrijving(models.Model):
    class Meta:
        verbose_name_plural = "Dossier Document Beschrijvingen"

    # dossier_naam = models.ForeignKey('talen.Label', on_delete=models.CASCADE)
    dossier_naam = models.CharField(max_length=100)

    def __str__(self):
        return self.dossier_naam
