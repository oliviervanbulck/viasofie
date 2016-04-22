from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Land(models.Model):
    class Meta:
        verbose_name_plural = "Landen"
    naam = models.CharField(max_length=255)
    landcode = models.CharField(max_length=2)

    def __str__(self):
        return str(self.naam) + ' - ' + str(self.landcode)


class Adres(models.Model):
    class Meta:
        verbose_name_plural = "Adressen"
    straat = models.CharField(max_length=255)
    huisnummer = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    gemeente = models.CharField(max_length=255)
    land = models.ForeignKey('Land', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s, %s %s' % (str(self.straat), str(self.huisnummer), str(self.postcode), str(self.gemeente))


#Gebruiker is extent van User object
class Gebruiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    telefoonnummer = models.CharField(max_length=255)
    adres = models.OneToOneField('Adres', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s (%s)' % (str(self.user.first_name), str(self.user.last_name), str(self.user.email))
