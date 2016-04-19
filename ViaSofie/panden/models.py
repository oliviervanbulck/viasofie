from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Pand(models.Model):
    prijs = models.FloatField()
    test = models.FloatField()