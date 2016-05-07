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


def chunks(l, n):
    """
    Source: http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    return [l[i:i+n] for i in xrange(0, len(l), n)]


def get_alle_actieve_panden_in_rijen(panden_per_rij):
    """
    vul_op_met_none -> als er niet voldoende panden zijn om de laatste rij vol te krijen, wordt die verder opgevuld met None
    """
    rijen = chunks(Pand.objects.filter(dossier__actief=True), panden_per_rij)
    return rijen

