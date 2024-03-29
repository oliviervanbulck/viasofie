# Models voor gebruikers gebaseerd op het ERD

from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible


# ERD tabel Landen
@python_2_unicode_compatible
class Land(models.Model):
    class Meta:
        verbose_name_plural = "landen"

    naam = models.CharField(max_length=255)
    landcode = models.CharField(max_length=2)

    def __str__(self):
        return '%s - %s' % (str(self.landcode), self.naam)


# ERD Woonplaats
class Woonplaats(models.Model):
    class Meta:
        verbose_name_plural = "woonplaatsen"

    postcode = models.CharField(max_length=10)
    gemeente = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s' % (self.postcode, self.gemeente)


@python_2_unicode_compatible
# ERD tabel Adres
class Adres(models.Model):
    class Meta:
        verbose_name_plural = "adressen"

    straat = models.CharField(max_length=255)
    huisnummer = models.CharField(max_length=10)
    woonplaats = models.ForeignKey('Woonplaats', on_delete=models.CASCADE)
    land = models.ForeignKey('Land', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s, %s %s' % (self.straat, self.huisnummer, self.woonplaats.postcode, self.woonplaats.gemeente)


# Gebruiker is extent van User object
@python_2_unicode_compatible
class Gebruiker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    telefoonnummer = models.CharField(max_length=255)
    adres = models.ForeignKey('Adres', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s (%s)' % (self.user.first_name, self.user.last_name, self.user.email)


# Mailtje wordt naar de user gestuurd wanneer zijn account wordt aangemaakt.
@receiver(post_save, sender=User)
def auto_mail_user_on_save(sender, instance, **kwargs):
    if kwargs.get('raw'):
        print "1"
        return
    if not instance.pk:
        print "2"
        return False

    # Enkel mailen bij aanmaken account
    if kwargs['created']:
        print "3"
        # Username = email!!!
        email = EmailMessage('Uw account is klaar',
                             'Uw account op ViaSofie.be is aangemaakt. Gelieve je wachtwoord hier in te stellen: http://' + str(Site.objects.get_current()) + reverse('password_reset'),
                             to=[instance.username])
        email.send()


# Oplossing om e-mail als username te gebruiken
@receiver(models.signals.pre_save, sender=User)
def auto_fill_in_email(sender, instance, **kwargs):
    instance.email = instance.username
