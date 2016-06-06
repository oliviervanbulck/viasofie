from __future__ import unicode_literals

from django.db import models


class FaqItem(models.Model):
    class Meta:
        verbose_name = 'FAQ item'
    titel = models.CharField(max_length=255)
    tekst = models.TextField()