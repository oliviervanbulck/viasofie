from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Label(models.Model):
    class Meta:
        verbose_name_plural = "Labels"
    naam = models.CharField(max_length=255)


class Taalcode(models.Model):
    class Meta:
        verbose_name_plural = "Taalcodes"
    taalcode = models.CharField(max_length=5)


class TaalcodePerLabel(models.Model):
    class Meta:
        unique_together = (('label', 'taalcode',),)
        verbose_name_plural = "Vertalingen"
    vertaling = models.CharField(max_length=255)
    label = models.ForeignKey('Label', on_delete=models.CASCADE)
    taalcode = models.ForeignKey('Taalcode', on_delete=models.CASCADE)
