from __future__ import unicode_literals

from django.db import models


class FaqItem(models.Model):
    class Meta:
        verbose_name = 'FAQ item'
    actief = models.BooleanField(default=True)
    titel = models.CharField(max_length=255)
    tekst = models.TextField()


class Partner(models.Model):
    actief = models.BooleanField()
    naam = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ImageField()
