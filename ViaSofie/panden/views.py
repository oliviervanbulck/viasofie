from django.http import HttpResponseRedirect
from django.shortcuts import render
from ViaSofie.functions import get_alle_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from ViaSofie.functions import keyword_search
from .models import Pand
from .models import Type
from .forms import AdvancedSearchForm


def panden_general(request, nbar_val):
    def check_get_parameters():
        required_params = ['gemeente', 'soort', 'zwembad', 'tuin', 'slaapkamer_lower', 'slaapkamer_upper', 'prijs_lower', 'prijs_upper']
        for param in required_params:
            if param not in request.GET:
                return False
        return True

    pand_types = Type.objects.all()
    gemeentes = get_alle_gemeentes()

    context = {
        'nbar': nbar_val,
        'pand_types': pand_types,
        'gemeentes': gemeentes,
        'form': AdvancedSearchForm()
    }

    if request.POST and request.POST['search'] and ('clearPanden' not in request.POST):
        panden = keyword_search(Pand, request.POST['search'],
                                ('adres__straat', 'adres__gemeente', 'adres__postcode', 'adres__huisnummer',
                                 'type__type',))
        context['search'] = request.POST['search']
    elif check_get_parameters():
        # Make sure the form doesn't reset
        context['form'] = AdvancedSearchForm(request.GET)

        panden = get_alle_actieve_panden()

        # Prijs filter
        panden = [pand for pand in panden if int(request.GET['prijs_lower']) <= pand.prijs <= int(request.GET['prijs_upper'])]

        # Slaapkamers filter
        panden = [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming='Aantal slaapkamers')
                  and (int(request.GET['slaapkamer_lower']) <= pand.pandkenmerkperpand_set.filter(kenmerk__benaming='Aantal slaapkamers')[0].aantal <= int(request.GET['slaapkamer_upper']))]

        # Gemeente filter
        if request.GET['gemeente'] != '':
            panden = [pand for pand in panden if pand.adres.gemeente == request.GET['gemeente']]

        # Soort filter
        if request.GET['soort'] != '':
            panden = [pand for pand in panden if pand.type.type == request.GET['soort']]

        # Zwembad filter
        zwembad = request.GET['zwembad']
        ZWEMBAD_KENMERK = 'Zwembad'
        if zwembad != 'eender':
            if zwembad == 'ja':
                panden = [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                          and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)[0].aantal == 1]
            else:
                panden = [pand for pand in panden if not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                          or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)
                              and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=ZWEMBAD_KENMERK)[0].aantal == 0)]

        tuin = request.GET['tuin']
        TUIN_KENMERK = 'Oppervlakte tuin'
        if tuin != 'eender':
            if tuin == 'ja':
                panden = [pand for pand in panden if pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                          and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)[0].aantal > 0]
            else:
                panden = [pand for pand in panden if not pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                          or (pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)
                              and pand.pandkenmerkperpand_set.filter(kenmerk__benaming=TUIN_KENMERK)[0].aantal == 0)]
    else:
        panden = get_alle_actieve_panden()
    context['pand_kolom_class'] = 'col-lg-4 col-md-6'
    context['panden'] = panden

    return render(request, 'panden/index.html', context)


# Create your views here.
def index(request):
    return panden_general(request, 'kopen')


def huren(request):
    return panden_general(request, 'huren')


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'pand': pand
    }
    return render(request, 'panden/pand_detail.html', context)
