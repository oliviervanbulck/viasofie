from django.contrib.auth.models import Group, Permission
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.
from django.template import RequestContext

from panden.models import Foto, CarouselFoto
from .functions import get_random_actieve_panden
from .forms import ContactForm


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    AANTAL_PANDEN = 3

    foto = Foto.objects.first()
    carousel_fotos = CarouselFoto.objects.filter(actief=True)
    panden = get_random_actieve_panden(AANTAL_PANDEN)
    aantal_panden = len(panden)
    pand_kolom_class = ''
    if aantal_panden != 0:
        pand_kolom_class = 'col-md-' + str(12 / aantal_panden)  # 12 is het aantal kolommen in Bootstrap

    context = {
        'panden': panden,
        'aantal_panden': aantal_panden,
        'pand_kolom_class': pand_kolom_class,
        'foto': foto,
        'nbar': 'home',
        'carousel': carousel_fotos,
    }

    return render(request, 'ViaSofie/index.html', context)


def about(request):
    return render(request, 'ViaSofie/about.html', {'nbar': 'about'})


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                email = EmailMessage('', email + '\n\n' + message, to=['michael.vanderborght.mv@gmail.com'])
                email.send()
                return render(request, 'ViaSofie/contact.html', {'nbar': 'contact', 'succes': True,'form': ContactForm()})
            else:
                raise Exception()
        except:
            return render(request, 'ViaSofie/contact.html', {'nbar': 'contact', 'error': True, 'form': form})
    else:
        form = ContactForm()

    return render(request, 'ViaSofie/contact.html', {'form': form})


def services(request):
    return render(request, 'ViaSofie/services.html', {})


def faq(request):
    return render(request, 'ViaSofie/faq.html', {'nbar': 'faq'})


def disclaimer(request):
    return render(request, 'ViaSofie/disclaimer.html', {'nbar': 'disclaimer'})


