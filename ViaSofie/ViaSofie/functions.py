from panden.models import Pand
from gebruikers.models import Adres
import random


def get_random_actieve_panden(aantal):
    panden = Pand.objects.filter(dossier__actief=True)
    return random.sample(panden, min(aantal, len(panden)))


# Kan mogelijk efficienter
def get_alle_gemeentes():
    tmp = Adres.objects.values('gemeente').distinct()
    returnable = []
    for gemeente in tmp:
        returnable.append(gemeente['gemeente'])
    return returnable
