from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext

from panden.models import Foto
from .functions import get_random_actieve_panden


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    AANTAL_PANDEN = 3

    foto = Foto.objects.first()
    panden = get_random_actieve_panden(AANTAL_PANDEN)

    context = {
        'panden': panden,
        'aantal_panden': len(panden),
        'foto': foto,
        'nbar': 'home'
    }

    return render(request, 'ViaSofie/index.html', context)


def about(request):
    return render(request, 'ViaSofie/about.html', {'nbar': 'about'})


def contact(request):
    return render(request, 'ViaSofie/contact.html', {'nbar': 'contact'})


def services(request):
    return render(request, 'ViaSofie/services.html', {})

