from django.shortcuts import render
from django.template import loader
from ViaSofie.functions import get_random_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from .models import Pand
from .models import Type


# Create your views here.
def index(request):
    test = "Hello world!"
    panden = get_random_actieve_panden(1)
    pand_types = Type.objects.all()
    gemeentes = get_alle_gemeentes()

    context = {
        'test': test,
        'nbar': 'panden',
        'panden': panden,
        'pand_types': pand_types,
        'gemeentes': gemeentes,
    }
    return render(request, 'panden/index.html', context)


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'pand': pand
    }
    return render(request, 'panden/pand_detail.html', context)