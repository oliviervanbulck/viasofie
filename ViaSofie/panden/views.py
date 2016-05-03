from django.shortcuts import render
from django.template import loader
from ViaSofie.functions import get_random_actieve_panden
from .models import Pand


# Create your views here.
def index(request):
    test = "Hello world!"
    panden = get_random_actieve_panden(1)
    context = {
        'test': test,
        'nbar': 'panden',
        'panden': panden
    }
    return render(request, 'panden/index.html', context)


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'pand': pand
    }
    return render(request, 'panden/pand_detail.html', context)