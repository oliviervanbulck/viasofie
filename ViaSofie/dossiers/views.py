from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.core.urlresolvers import reverse
from ViaSofie.templatetags.viasofie_filters import in_euro, in_opp

from dossiers.forms import ContactFormDossier
from panden.models import Pand


def index(request):
    panden = request.user.gebruiker.pand_set.all()
    context = {
        'panden': panden,
        'dossier': True,
        'nbar': 'dossier'
    }
    return render(request, "Dossier/index.html", context)


def dossier(request, pand_id):
    if request.user.is_authenticated():
        #dossier_obj = Dossier.objects.get(id=dossier_id)
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
                context.update({'nbar': 'dossier'})
                return render(request, "Dossier/dossier.html", context)

            elif request.method == 'POST':
                form = ContactFormDossier(request.POST)

                try:
                    if form.is_valid():
                        email = request.user.email
                        message = form.cleaned_data['message']
                        email = EmailMessage('', email + '\n\n' + message, to=['michael.vanderborght.mv@gmail.com'])
                        email.send()
                        context.update({'succes': True, 'form': ContactFormDossier()})
                        return render(request, context, 'Dossier/dossier.html',context)
                    else:
                        raise Exception()
                except:
                    context.update({'error': True, 'form': form})
                    return render(request, 'Dossier/dossier.html', context)
        else:
            return redirect('dossiers.index')
    else:
        # Redirect the user to the login if he's not logged in
        return redirect(reverse('index') + '?le=3')