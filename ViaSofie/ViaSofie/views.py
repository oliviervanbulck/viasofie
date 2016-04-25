from django.shortcuts import render


# Create your views here.
from panden.models import Foto


def index(request):
    foto = Foto.objects.first()
    return render(request, 'ViaSofie/index.html', {'foto': foto})


def about(request):
    return render(request, 'ViaSofie/about.html', {})


def contact(request):
    return render(request, 'ViaSofie/contact.html', {})


def services(request):
    return render(request, 'ViaSofie/services.html', {})
