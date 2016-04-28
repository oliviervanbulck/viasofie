from django.shortcuts import render

# Create your views here.
from panden.models import Foto
from panden.models import Pand
from .functions import get_random_actieve_panden

import random


def index(request):
    AANTAL_PANDEN = 3

    foto = Foto.objects.first()

    context = {
        'panden': get_random_actieve_panden(AANTAL_PANDEN),
        'foto': foto,
    }

    return render(request, 'ViaSofie/index.html', context)


def about(request):
    return render(request, 'ViaSofie/about.html', {})


def contact(request):
    return render(request, 'ViaSofie/contact.html', {})


def services(request):
    return render(request, 'ViaSofie/services.html', {})

