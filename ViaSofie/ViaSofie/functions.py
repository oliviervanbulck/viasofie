from panden.models import Pand
from gebruikers.models import Adres
import random


def get_random_actieve_panden(aantal):
    panden = Pand.objects.filter(dossier__actief=True)
    return random.sample(panden, min(aantal, len(panden)))


# Kan mogelijk efficienter
def get_alle_gemeentes():
    # Vreemde data is gereturned als het anders wordt uitgevoerd (volledige objecten van adres)
    return [gemeente['gemeente'] for gemeente in Adres.objects.values('gemeente').distinct()]


def get_alle_actieve_panden():
    rij = Pand.objects.filter(dossier__actief=True)
    return rij
