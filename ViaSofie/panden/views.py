from django.http import HttpResponseRedirect
from django.shortcuts import render
from ViaSofie.functions import get_alle_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from ViaSofie.functions import keyword_search
from ViaSofie.functions import advanced_search
from .models import Pand
from .models import Type
from .forms import AdvancedSearchForm


def panden_general(request, nbar_val):
    def check_get_parameters():
        required_params = ['prijs_upper', 'prijs_lower', 'gemeente', 'oppervlakte_upper', 'oppervlakte_lower',
                           'type', 'slaapkamer_lower', 'badkamer_lower', 'parking', 'terras', 'tuin',
                           'bemeubeld', 'bouwjaar']
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

        # Filter op de juiste panden
        panden = advanced_search(request)
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
