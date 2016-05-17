# Models voor panden gebaseerd op het ERD

from __future__ import unicode_literals

import os

from django.contrib import admin
from django.db import models


# Create your models here.

# ERD tabel Type
from django.db.models.signals import pre_delete
from django.dispatch import receiver
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
    is_aantal = models.BooleanField()

    def __str__(self):
        return str(self.benaming)


@python_2_unicode_compatible
# ERD tabel Pand
class Pand(models.Model):
    class Meta:
        verbose_name_plural = "Panden"
    prijs = models.FloatField()
    bouwjaar = models.PositiveSmallIntegerField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    gebruiker = models.ForeignKey('gebruikers.Gebruiker', on_delete=models.CASCADE)
    adres = models.OneToOneField('gebruikers.Adres', on_delete=models.CASCADE, null=True)
    kenmerken = models.ManyToManyField('Kenmerk', through='PandKenmerkPerPand')

    def __str__(self):
        return str(self.type) + ' - ' + str(self.adres)


# ERD tabel PandImmoLink
class PandImmoLink(models.Model):
    class Meta:
        verbose_name_plural = "Immolinks"
    site_beschrijving = models.CharField(max_length=255, verbose_name='beschrijving')
    site_link = models.CharField(max_length=255, verbose_name='link')
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


@receiver(models.signals.post_delete, sender=Foto)
def auto_delete_foto_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if kwargs.get('raw'):
        return
    if instance.foto:
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)


@receiver(models.signals.pre_save, sender=Foto)
def auto_delete_foto_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if kwargs.get('raw'):
        return
    if not instance.pk:
        return False

    try:
        old_file = Foto.objects.get(pk=instance.pk).foto
    except Foto.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


# ERD tabel CarouselFoto
class CarouselFoto(models.Model):
    class Meta:
        verbose_name_plural = "Slideshow"
        verbose_name = "foto voor slideshow"

    foto = models.ImageField()
    actief = models.BooleanField(default=True)

    def __str__(self):
        return self.foto.url

    def get_admin_url(self):
        return "/admin/panden/carousel-foto/%d/" % self.id


@receiver(models.signals.post_delete, sender=CarouselFoto)
def auto_delete_carousel_foto_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if kwargs.get('raw'):
        return
    if instance.foto:
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)


@receiver(models.signals.pre_save, sender=CarouselFoto)
def auto_delete_carousel_foto_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is changed.
    """
    if kwargs.get('raw'):
        return
    if not instance.pk:
        return False

    try:
        old_file = Foto.objects.get(pk=instance.pk).foto
    except CarouselFoto.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


# ERD tabel PandKenmerkPerPand
class PandKenmerkPerPand(models.Model):
    class Meta:
        unique_together = (('pand', 'kenmerk'),)
        verbose_name_plural = "Pandkenmerken"
        verbose_name = 'Pandkenmerk'
    aantal = models.PositiveSmallIntegerField()
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)
    kenmerk = models.ForeignKey('Kenmerk', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kenmerk) + ' - ' + str(self.aantal) + ' - ' + str(self.pand)
