import os
from email.mime.image import MIMEImage

from django.shortcuts import render, render_to_response
from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.template import RequestContext
from django.template.loader import render_to_string

from panden.models import CarouselFoto
from .models import Partner, FaqItem
from .functions import get_recente_panden
from .forms import ContactForm

from ViaSofie.settings import EMAIL_CONTACT


# Foutpagina wanneer pagina niet werd gevonden
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


# Startpagina
def index(request):
    carousel_fotos = CarouselFoto.objects.filter(actief=True)
    partners = Partner.objects.filter(actief=True).order_by('-prioriteit')
    panden = get_recente_panden()

    context = {
        'panden': panden,
        'nbar': 'home',
        'carousel': carousel_fotos,
        'partners': partners,
    }
    if request.POST:
        email_address = request.POST.get('email')
        message = "heeft een e-book aangevraagd."
        email = EmailMessage('E-book', email_address + ' ' + message, to=[EMAIL_CONTACT])
        email.send()

    if request.GET.get('le') is not None:
        context['loginerror'] = request.GET.get('le')

    response = render(request, 'ViaSofie/index.html', context)

    return response


# Over ons pagina
def about(request):
    return render(request, 'ViaSofie/about.html', {'nbar': 'about'})


# Contactpagina
def contact(request):
    context = {
        'nbar': 'contact',
        'form': ContactForm(),
    }

    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                email_address = form.cleaned_data['email']
                message = form.cleaned_data['message']
                email = EmailMessage('', email_address + '\n\n' + message, to=[EMAIL_CONTACT])
                email.send()

                bev_content_text = 'Welkom bij Via Sofie! \n\n Wij hebben uw mail goed ontvangen. \n U mag spoedig een antwoord van ons verwachten.\n\n Vriendelijke groet, \n\n Sofie'

                msg = EmailMultiAlternatives("Contactverzoek", bev_content_text,
                                             EMAIL_CONTACT, [email_address])

                msg.attach_alternative(render_to_string('ViaSofie/email/contact_confirmation.html'), "text/html")

                msg.mixed_subtype = 'related'

                for f in ['ContactBevestiging.jpg']:
                    print os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'static'), 'ViaSofie'), f)
                    fp = open(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'static'), 'ViaSofie'), f), 'rb')
                    msg_img = MIMEImage(fp.read())
                    fp.close()
                    msg_img.add_header('Content-ID', '<{}>'.format(f))
                    msg.attach(msg_img)

                msg.send()

                context['succes'] = True
            else:
                raise Exception()
        except:
            context['error'] = True
            context['form'] = form

    return render(request, 'ViaSofie/contact.html', context)


# Adviespagina
def faq(request):
    context = {
        'nbar': 'faq',
        'faq_items': FaqItem.objects.filter(actief=True).order_by('-prioriteit'),
    }

    return render(request, 'ViaSofie/faq.html', context)


# Disclaimer/privacy pagina
def legal(request):
    if request.GET.get('on') and (request.GET.get('on') == 'disclaimer' or request.GET.get('on') == 'privacy'):
        page = request.GET['on']
    else:
        page = 'disclaimer'
    return render(request, 'ViaSofie/disclaimer.html', {'nbar': page, 'default': page})
