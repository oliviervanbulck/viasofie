from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Land(models.Model):
    class Meta:
        verbose_name_plural = "Landen"
    naam = models.CharField(max_length=255)
    landcode = models.CharField(max_length=2)

    def __str__(self):
        return '%s - %s' % (str(self.landcode), self.naam)


@python_2_unicode_compatible
class Adres(models.Model):
    class Meta:
        verbose_name_plural = "Adressen"
    straat = models.CharField(max_length=255)
    huisnummer = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    gemeente = models.CharField(max_length=255)
    land = models.ForeignKey('Land', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s, %s %s' % (self.straat, self.huisnummer, self.postcode, self.gemeente)


# Gebruiker is extent van User object
class Gebruiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    telefoonnummer = models.CharField(max_length=255)
    adres = models.ForeignKey('Adres', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s (%s)' % (str(self.user.first_name), str(self.user.last_name), str(self.user.email))
