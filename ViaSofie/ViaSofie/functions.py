from django.db.models import Q

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


def keyword_search(model, keywords, search_fields):
    """Search according to fields defined in Admin's search_fields"""
    all_queries = None

    for keyword in keywords.split(' '):
        keyword_query = None

        for field in search_fields:
            each_query = Q(**{field+'__icontains': keyword})

            if not keyword_query:
                keyword_query = each_query
            else:
                keyword_query = keyword_query | each_query

        if not all_queries:
            all_queries = keyword_query
        else:
            all_queries = all_queries & keyword_query

    result_set = model.objects.filter(all_queries).distinct()

    return result_set
