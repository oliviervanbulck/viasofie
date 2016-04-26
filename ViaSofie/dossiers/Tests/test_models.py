from django.test import TestCase
from dossiers.models import *
from panden.models import Pand, Type, Kenmerk, PandKenmerkPerPand
from gebruikers.models import *

from datetime import datetime

class DossiersTestCase(TestCase):
    def setUp(self):
        print 'yuuuuu'

        # Dossier setup
        testKenmerk = Kenmerk.objects.create(benaming="aantalBadkamers")
        testUser = User.objects.create(username="Bartje", email="bartje@nva.be")

        testLand = Land.objects.create(naam="Belgie",landcode="BE")
        testAdres = Adres.objects.create(straat="nepstraat",
                                         huisnummer="123",
                                         postcode=2000,
                                         gemeente="Antwerpen",
                                         land=testLand)
        testGebruiker = Gebruiker.objects.create(user=testUser,
                                                 telefoonnummer="04040404",
                                                 adres=testAdres)
        testType1 = Type.objects.create(type="Dikke villa")
        testPand1 = Pand.objects.create(prijs=10000.10,
                                        bouwjaar=datetime.today(),
                                        oppervlakte=125,
                                        type=testType1,
                                        gebruiker=testGebruiker,
                                        adres=testAdres)
        Dossier.objects.create(actief=True,pand=testPand1)
        print 'ayyyyy'

    def test_dossier(self):
        print Dossier.objects.all()
        dossier = Dossier.objects.first()
        self.assertEqual(dossier.pand.prijs, 10000.10)
