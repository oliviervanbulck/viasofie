from __future__ import unicode_literals

import os
from django.db import models
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class FaqItem(models.Model):
    class Meta:
        verbose_name = 'FAQ item'
    actief = models.BooleanField(default=True)
    titel = models.CharField(max_length=255)
    tekst = models.TextField()
    prioriteit = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.titel


@python_2_unicode_compatible
class Partner(models.Model):
    actief = models.BooleanField(default=True)
    naam = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ImageField(upload_to='partner-img')
    prioriteit = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.naam


@receiver(models.signals.post_delete, sender=Partner)
def auto_delete_logo_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if kwargs.get('raw'):
        return
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)
