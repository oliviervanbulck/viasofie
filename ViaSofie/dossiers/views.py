import os
from email.mime.image import MIMEImage

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from ViaSofie.templatetags.viasofie_filters import in_euro, in_opp

from dossiers.forms import ContactFormDossier
from panden.models import Pand
from ViaSofie.settings import BASE_DIR, EMAIL_CONTACT, EMAIL_DRINGEND


@login_required()
def index(request):
    panden = request.user.gebruiker.pand_set.all()
    context = {
        'panden': panden,
        'dossier': True,
        'nbar': 'dossier'
    }
    return render(request, "Dossier/index.html", context)


@login_required()
def dossier(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    if request.user.id == pand.gebruiker.user.id:
        doclijnen = pand.dossierdoclijn_set.all()
        stavaza = pand.stavazalijn_set.all()

        context = {
            'pand': pand,
            'ref_nummer': pand.ref_number(),
            'basis_kenmerken': [(pand.adres, 'Adres'), (in_euro(pand.prijs), 'Prijs'), (pand.type, 'Type'),
                                (pand.bouwjaar, 'Bouwjaar'), (in_opp(pand.oppervlakte), 'Oppervlakte'),
                                (pand.algemene_beschrijving, 'Beschrijving')],
            'kenmerken': pand.pandkenmerkperpand_set.all().order_by('kenmerk__benaming'),
            'foto': pand.foto_set.first(),
            'doclijnen': doclijnen,
            'stavazalijnen': stavaza,
            'form': ContactFormDossier(),
            'prev_url': request.META.get('HTTP_REFERER', None),
        }
        if request.method == 'GET':
            context['nbar'] = 'dossier'
            return render(request, "Dossier/dossier.html", context)

        elif request.method == 'POST':
            form = ContactFormDossier(request.POST, request.FILES)

            try:
                if form.is_valid():
                    email_address = request.user.email
                    message = form.cleaned_data['message']
                    attachment = request.FILES.get('attachment')
                    email = EmailMessage('', email_address + '\n\n' + message, to=[EMAIL_DRINGEND])
                    if attachment:
                        email.attach(attachment.name, attachment.read(), attachment.content_type)
                    email.send()

                    bev_content_text = 'Welkom bij Via Sofie! \n\n Wij hebben uw mail goed ontvangen. \n U mag spoedig een antwoord van ons verwachten.\n\n Vriendelijke groet, \n\n Sofie'
                    # bev_content_html = '<img src="cid:logo.png" alt="Logo Via Sofie" />Welkom bij Via Sofie! \n\n Wij hebben uw mail goed ontvangen. \n U mag spoedig een antwoord van ons verwachten.\n\n Vriendelijke groet, \n\n Sofie'

                    msg = EmailMultiAlternatives("Contactverzoek", bev_content_text,
                                                 EMAIL_CONTACT, [email_address])

                    msg.attach_alternative(render_to_string('ViaSofie/email/contact_confirmation.html'), "text/html")

                    msg.mixed_subtype = 'related'

                    for f in ['ContactBevestiging.jpg']:
                        """print os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'static'), 'ViaSofie'),
                                           f)"""
                        print os.path.join(os.path.join(os.path.join(os.path.join(BASE_DIR, 'ViaSofie'), 'static'), 'ViaSofie'), f)
                        fp = open(
                            os.path.join(
                                os.path.join(os.path.join(os.path.join(BASE_DIR, 'ViaSofie'), 'static'), 'ViaSofie'), f), 'rb')
                        msg_img = MIMEImage(fp.read())
                        fp.close()
                        msg_img.add_header('Content-ID', '<{}>'.format(f))
                        msg.attach(msg_img)

                    msg.send()

                    context.update({'succes': True, 'form': ContactFormDossier()})
                    return render(request, context, 'Dossier/dossier.html',context)
                else:
                    raise Exception()
            except:
                context.update({'error': True, 'form': form})
                return render(request, 'Dossier/dossier.html', context)
    else:
        return redirect('dossiers.index')
