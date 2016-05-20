from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from dossiers.models import Dossier
from panden.models import Pand


def index(request):
    panden = request.user.gebruiker.pand_set.all()
    context = {
        'panden': panden
    }
    return render(request, "Dossier/index.html", context)


def dossier(request, dossier_id):
    dossier_obj = Dossier.objects.get(id=dossier_id)
    pand = Pand.objects.get(id=dossier_obj.pand_id)
    doclijnen = dossier_obj.dossierdoclijn_set.all()
    context = {
        'dossier':dossier_obj,
        'basis_kenmerken': [(pand.adres, 'Adres'),(pand.prijs, 'Prijs'),(pand.type, 'Type'),(pand.bouwjaar, 'Bouwjaar'),(pand.oppervlakte, 'Oppervlakte')],
        'kenmerken':pand.pandkenmerkperpand_set.all().order_by('kenmerk__benaming'),
        'foto':pand.foto_set.first(),
        'doclijnen':doclijnen,
    }
    return render(request, "Dossier/dossier.html",context)

#def testje(request, dossier_id):
    #return HttpResponse('ayyyyy' + dossier_id)