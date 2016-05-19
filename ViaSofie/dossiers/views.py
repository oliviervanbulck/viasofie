from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    panden = request.user.gebruiker.pand_set.all()
    context = {
        'panden': panden
    }
    return render(request, "Dossier/index.html", context)


def dossier(request):

    context = {
        'dossier_id'
    }
    return render(request, "Dossier/dossier.html")

def testje(request, dossier_id):
    return HttpResponse('ayyyyy' + dossier_id)