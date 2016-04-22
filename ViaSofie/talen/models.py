from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


class Label(models.Model):
    class Meta:
        verbose_name_plural = "Labels"
    naam = models.CharField(max_length=255)

    def __str__(self):
        return self.naam


class Taalcode(models.Model):
    class Meta:
        verbose_name_plural = "Taalcodes"
    taalcode = models.CharField(max_length=5)

    def __str__(self):
        return self.taalcode


@python_2_unicode_compatible
class TaalcodePerLabel(models.Model):
    class Meta:
        unique_together = (('label', 'taalcode',),)
        verbose_name_plural = "Vertalingen"
    vertaling = models.CharField(max_length=255)
    label = models.ForeignKey('Label', on_delete=models.CASCADE)
    taalcode = models.ForeignKey('Taalcode', on_delete=models.CASCADE)

    def __str__(self):
        return self.label.naam + ' - ' + self.taalcode.taalcode
