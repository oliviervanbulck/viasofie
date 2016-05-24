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
    """Filter voor prijs"""
    def filter_prijs(panden):
        LOWER = int(request.GET['prijs_lower'])
        UPPER = int(request.GET['prijs_upper'])

        for pand in panden:
            print "Hmmm: " + str(pand.pandkenmerkperpand_set)
            print "Hmmm: " + str(pand.kenmerken)

        return [pand for pand in panden if
                LOWER <= pand.prijs <= UPPER]

    """Filter voor gemeente"""
    def filter_gemeente(panden):
        if request.GET['gemeente'] != 'nvt':
            return [pand for pand in panden if pand.adres.woonplaats.gemeente == request.GET['gemeente']]
        return panden

    """Filter voor oppervlakte"""
    def filter_oppervlake(panden):
        LOWER = int(request.GET['oppervlakte_lower'])
        UPPER = int(request.GET['oppervlakte_upper'])
        return [pand for pand in panden if
                LOWER <= pand.oppervlakte <= UPPER]

    """Filter voor type"""
    def filter_type(panden):
        if request.GET['type'] != 'nvt':
            return [pand for pand in panden if pand.type.type == request.GET['type']]
        return panden

    """Filter voor aantal slaapkamer"""
    def filter_slaapkamers(panden):
        BENAMING = 'Aantal slaapkamers'
        LOWER = int(request.GET['slaapkamer_lower'])

        print LOWER
        for pand in panden:
            print pand.pandkenmerkperpand_set
            print pand.kenmerken

            """test = pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
            if test:
                print str(pand) + str(test[0].aantal)"""

        return [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                and (LOWER <= pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal)]

    """Filter voor badkamers"""
    def filter_badkamers(panden):
        BENAMING = 'Aantal badkamers'
        LOWER = int(request.GET['badkamer_lower'])

        print LOWER
        """for pand in panden:
            print pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal"""

        return [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                and (LOWER <= pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal)]

    """Filter voor Parking / Garage"""
    def filter_parking(panden):
        parking = request.GET['parking']
        BENAMING = 'Parking / Garage'
        if parking != 'nvt':
            if parking == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal > 0]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[
                                0].aantal == 0)]
        return panden

    """Filter voor Terras"""
    def filter_terras(panden):
        terras = request.GET['terras']
        BENAMING = 'Terras'
        if terras != 'nvt':
            if terras == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal > 0]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[
                                0].aantal == 0)]
        return panden

    """Filter voor tuin"""
    def filter_tuin(panden):
        tuin = request.GET['tuin']
        BENAMING = 'Oppervlakte tuin'
        if tuin != 'nvt':
            if tuin == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal > 0]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[
                                0].aantal == 0)]
        return panden

    """Filter voor bemeubeld"""
    def filter_bemeubeld(panden):
        bemeubeld = request.GET['bemeubeld']
        BENAMING = 'Bemeubeld'
        if bemeubeld != 'nvt':
            if bemeubeld == 'ja':
                return [pand for pand in panden if
                        pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal > 0]
            else:
                return [pand for pand in panden if
                        not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                        or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)
                            and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=BENAMING)[0].aantal == 0)]
        return panden

    """Filter bouwjaar"""
    def filter_bouwjaar(panden):
        BENAMING = int(request.GET['bouwjaar'])
        return [pand for pand in panden if
                BENAMING <= pand.oppervlakte]

    """Combinatie van alle filters"""
    panden = get_alle_actieve_panden()
    filters = [filter_prijs,
               filter_gemeente,
               filter_oppervlake,
               filter_type,
               filter_slaapkamers,
               # filter_badkamers,
               filter_parking,
               # filter_terras,
               filter_tuin,
               filter_bemeubeld,
               filter_bouwjaar]

    # Elke filter maakt de gevonden panden specifieker en specifieker, maar als we met een lege lijst zitten moet er niet verder gefilterd worden (break)
    for filter in filters:
        print panden
        print filter.__name__
        if panden:
            panden = filter(panden)
        else:
            break
    return panden