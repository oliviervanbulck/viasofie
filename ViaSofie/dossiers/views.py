from django.core.mail import EmailMessage
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ViaSofie.templatetags.viasofie_filters import in_euro, in_opp

from dossiers.forms import ContactFormDossier
from panden.models import Pand


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
                    attachment = request.FILES['attachment']
                    email = EmailMessage('', email_address + '\n\n' + message, to=['dringend.viasofie@gmail.com'])
                    if attachment:
                        email.attach(attachment.name, attachment.read(), attachment.content_type)
                    email.send()

                    message_bevestiging = 'Welkom bij Via Sofie! \n\n Wij hebben uw mail goed ontvangen. \n U mag spoedig een antwoord van ons verwachten.\n\n Vriendelijke groet, \n\n Sofie'
                    email_bevestiging = EmailMessage('Contact verzoek', message_bevestiging, to=[email_address])
                    email_bevestiging.send()
                    context.update({'succes': True, 'form': ContactFormDossier()})
                    return render(request, context, 'Dossier/dossier.html',context)
                else:
                    raise Exception()
            except:
                context.update({'error': True, 'form': form})
                return render(request, 'Dossier/dossier.html', context)
    else:
        return redirect('dossiers.index')
