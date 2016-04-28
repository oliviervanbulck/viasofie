from panden.models import Pand
import random


def get_random_actieve_panden(aantal):
    panden = [pand for pand in Pand.objects.all() if pand.dossier.actief]
    return random.sample(panden, min(aantal, len(panden)))
