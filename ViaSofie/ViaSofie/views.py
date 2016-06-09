from django.shortcuts import render, render_to_response
from django.core.mail import EmailMessage

from django.template import RequestContext

from panden.models import Foto, CarouselFoto
from .models import Partner, FaqItem
from .functions import get_random_actieve_panden
from .functions import set_cookie
from .forms import ContactForm


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    AANTAL_PANDEN = 3

    carousel_fotos = CarouselFoto.objects.filter(actief=True)
    partners = Partner.objects.filter(actief=True).order_by('-prioriteit')
    panden = get_random_actieve_panden(AANTAL_PANDEN)

    context = {
        'panden': panden,
        'nbar': 'home',
        'carousel': carousel_fotos,
        'partners': partners,
    }

    if request.GET.get('le') is not None:
        context['loginerror'] = request.GET.get('le')

    response = render(request, 'ViaSofie/index.html', context)

    if request.GET.get('lang', None):
        set_cookie(response, 'langCookie', request.GET.get('lang'))

    return response


def about(request):
    return render(request, 'ViaSofie/about.html', {'nbar': 'about'})


def contact(request):
    context = {
        'nbar': 'contact',
        'form': ContactForm(),
    }

    if request.POST:
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                email = EmailMessage('', email + '\n\n' + message, to=['contact.viasofie@gmail.com'])
                email.send()

                context['succes'] = True
            else:
                raise Exception()
        except:
            context['error'] = True
            context['form'] = form

    return render(request, 'ViaSofie/contact.html', context)


def faq(request):
    context = {
        'nbar': 'faq',
        'faq_items': FaqItem.objects.filter(actief=True).order_by('-prioriteit'),
    }

    return render(request, 'ViaSofie/faq.html', context)


def legal(request):
    if request.GET.get('on') and (request.GET.get('on') == 'disclaimer' or request.GET.get('on') == 'privacy'):
        page = request.GET['on']
    else:
        page = 'disclaimer'
    return render(request, 'ViaSofie/disclaimer.html', {'nbar': page, 'default': page})


