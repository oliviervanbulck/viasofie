# Models voor panden gebaseerd op het ERD

from __future__ import unicode_literals

import os

from django.contrib import admin
from django.db import models

import qrcode
import StringIO

from django.db import models
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.sites.models import Site
from django.template.defaultfilters import slice_filter, upper

from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# ERD tabel Type


class Type(models.Model):
    class Meta:
        verbose_name_plural = "types"
    type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.type)


# ERD tabel Kenmerk
class Kenmerk(models.Model):
    class Meta:
        verbose_name_plural = "kenmerken"
    benaming = models.CharField(max_length=50)
    is_aantal = models.BooleanField()
    type = models.ForeignKey('KenmerkType', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.benaming_nl)


class KenmerkType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return str(self.type)


@python_2_unicode_compatible
# ERD tabel Pand
class Pand(models.Model):
    class Meta:
        verbose_name_plural = "panden"
    prijs = models.FloatField()
    bouwjaar = models.PositiveSmallIntegerField()
    oppervlakte = models.FloatField()
    algemene_beschrijving = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    gebruiker = models.ForeignKey('gebruikers.Gebruiker', on_delete=models.CASCADE)
    adres = models.OneToOneField('gebruikers.Adres', on_delete=models.CASCADE, null=True)
    kenmerken = models.ManyToManyField('Kenmerk', through='PandKenmerkPerPand')
    actief = models.BooleanField(default=True)

    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def ref_number(self):
        return slice_filter(self.type.type, ':3').upper() + '-' + "%03d" % self.id

    def get_absolute_url(self):
        return 'http://' + str(Site.objects.get_current()) + reverse('panden.detail', args=[str(self.id)])

    def generate_qrcode(self):
        if not self.qrcode:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=6,
                border=0,
            )
            qr.add_data(self.get_absolute_url())
            qr.make(fit=True)

            img = qr.make_image()

            buffer = StringIO.StringIO()
            img.save(buffer)
            filename = 'panden-%s.png' % self.id
            filebuffer = InMemoryUploadedFile(
                buffer, None, filename, 'image/png', buffer.len, None)
            self.qrcode.save(filename, filebuffer)

    def __str__(self):
        return str(self.type) + ' - ' + str(self.adres)


@receiver(models.signals.post_save, sender=Pand)
def auto_create_qr_code_on_save(sender, instance, **kwargs):
    """Voegt een QR code toe aan het pand bij opslaan"""
    instance.generate_qrcode()


@receiver(models.signals.post_delete, sender=Pand)
def auto_delete_qr_code_on_delete(sender, instance, **kwargs):
    """Verwijderd de QR code van een pand wanneer het pand wordt gedelete"""
    if not kwargs.get('raw'):
        if instance.qrcode:
            if os.path.isfile(instance.qrcode.path):
                os.remove(instance.qrcode.path)


# ERD tabel PandImmoLink
class PandImmoLink(models.Model):
    class Meta:
        verbose_name_plural = "immolinks"
    site_link = models.CharField(max_length=255, verbose_name='link')
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)
    website = models.ForeignKey('ImmoSite',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.website.site_beschrijving) + ' - ' + str(self.pand)


class ImmoSite(models.Model):
    site_beschrijving = models.CharField(max_length=255, verbose_name='beschrijving')
    logo = models.ImageField()

    def __str__(self):
        return str(self.site_beschrijving)


# ERD tabel Foto
class Foto(models.Model):
    class Meta:
        verbose_name_plural = "foto's"
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
        verbose_name_plural = "slideshow"
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
        verbose_name_plural = "pandkenmerken"
        verbose_name = 'pandkenmerk'
    aantal = models.PositiveSmallIntegerField()
    pand = models.ForeignKey('Pand', on_delete=models.CASCADE)
    kenmerk = models.ForeignKey('Kenmerk', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kenmerk) + ' - ' + str(self.aantal) + ' - ' + str(self.pand)


class Switch(models.Model):
    class Meta:
        verbose_name = 'optie'
        verbose_name_plural = 'opties'

    naam = models.CharField(max_length=20)
    waarde = models.BooleanField(default=False)
