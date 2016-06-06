from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver


class FaqItem(models.Model):
    class Meta:
        verbose_name = 'FAQ item'
    actief = models.BooleanField(default=True)
    titel = models.CharField(max_length=255)
    tekst = models.TextField()

    def __str__(self):
        return self.titel


@receiver(models.signals.pre_save, sender=FaqItem)
def auto_change_newline_to_br(sender, instance, **kwargs):
    """Verandert newlines bij opslaan naar <br>"""
    instance.tekst = instance.tekst.replace('\r\n', '<br>').replace('\r', '<br>').replace('\n', '<br>')


class Partner(models.Model):
    actief = models.BooleanField(default=True)
    naam = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ImageField(upload_to='partner-img')

    def __str__(self):
        return self.naam
