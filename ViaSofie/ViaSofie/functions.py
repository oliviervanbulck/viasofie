from django.db.models import Q

from panden.models import Pand
from gebruikers.models import Woonplaats
from gebruikers.models import Adres
import random


def get_random_actieve_panden(aantal):
    panden = Pand.objects.filter(actief=True)
    return random.sample(panden, min(aantal, len(panden)))


def get_alle_gemeentes():
    return Woonplaats.objects.all()


def get_alle_actieve_panden():
    rij = Pand.objects.filter(actief=True)
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


def advanced_search(request):
    def filter_prijs(panden):
        return [pand for pand in panden if
                int(request.GET['prijs_lower']) <= pand.prijs <= int(request.GET['prijs_upper'])]

    def filter_slaapkamers(panden):
        return [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming='Aantal slaapkamers')
                and (int(request.GET['slaapkamer_lower']) <=
                     pand.pandkenmerkperpand_set.filter(kenmerk__benaming='Aantal slaapkamers')[0].aantal <= int(
            request.GET['slaapkamer_upper']))]

    def filter_gemeente(panden):
        if request.GET['gemeente'] != '':
            return [pand for pand in panden if pand.adres.woonplaats.gemeente == request.GET['gemeente']]
        return panden

    def filter_soort(panden):
        if request.GET['soort'] != '':
            return [pand for pand in panden if pand.type.type == request.GET['soort']]
        return panden

    def filter_zwembad(panden):
        zwembad = request.GET['zwembad']
        ZWEMBAD_KENMERK = 'Zwembad'
        if zwembad != 'eender':
            if zwembad == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)[0].aantal == 1]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)[0].aantal == 0)]
        return panden

    def filter_tuin(panden):
        tuin = request.GET['tuin']
        TUIN_KENMERK = 'Oppervlakte tuin'
        if tuin != 'eender':
            if tuin == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)[0].aantal > 0]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)[
                                0].aantal == 0)]
        return panden

    panden = get_alle_actieve_panden()
    filters = [filter_prijs,
               filter_slaapkamers,
               filter_gemeente,
               filter_soort,
               filter_tuin,
               filter_zwembad]

    # Elke filter maakt de gevonden panden specifieker en specifieker, maar als we met een lege lijst zitten moet er niet verder gefilterd worden (break)
    for filter in filters:
        if panden:
            panden = filter(panden)
        else:
            break
    return panden