from panden.models import Pand
import random


def get_random_actieve_panden(aantal):
    panden = Pand.objects.filter(dossier__actief=True)
    return random.sample(panden, min(aantal, len(panden)))
