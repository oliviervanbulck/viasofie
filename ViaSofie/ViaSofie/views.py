from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from panden.models import Foto
from .functions import get_random_actieve_panden


def handler404(request):
    response = render_to_response('ViaSofie/templates/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


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

