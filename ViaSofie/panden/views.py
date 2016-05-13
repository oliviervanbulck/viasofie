from django.http import HttpResponseRedirect
from django.shortcuts import render
from ViaSofie.functions import get_alle_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from ViaSofie.functions import keyword_search
from .models import Pand
from .models import Type


# Create your views here.
def index(request):
    pand_types = Type.objects.all()
    gemeentes = get_alle_gemeentes()

    context = {
        'nbar': 'kopen',
        'pand_types': pand_types,
        'gemeentes': gemeentes,
    }

    if request.POST and request.POST['search'] and ('clearPanden' not in request.POST):
        panden = keyword_search(Pand, request.POST['search'],
                                ('adres__straat', 'adres__gemeente', 'adres__postcode', 'adres__huisnummer',
                                 'type__type',))
        context['search'] = request.POST['search']
    else:
        panden = get_alle_actieve_panden()
    context['pand_kolom_class'] = 'col-lg-4 col-md-6'
    context['panden'] = panden

    return render(request, 'panden/index.html', context)


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'pand': pand
    }
    return render(request, 'panden/pand_detail.html', context)
