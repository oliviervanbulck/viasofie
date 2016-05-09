from django.shortcuts import render
from ViaSofie.functions import get_alle_actieve_panden_in_rijen
from ViaSofie.functions import get_alle_gemeentes
from .models import Pand
from .models import Type


# Create your views here.
def index(request):
    test = "Hello world!"
    pand_types = Type.objects.all()
    gemeentes = get_alle_gemeentes()

    PANDEN_PER_RIJ = 3
    panden_rijen = get_alle_actieve_panden_in_rijen(PANDEN_PER_RIJ)
    pand_kolom_class = 'col-md-' + str(12 / PANDEN_PER_RIJ)

    context = {
        'test': test,
        'nbar': 'kopen',
        'panden_rijen': panden_rijen,
        'pand_types': pand_types,
        'gemeentes': gemeentes,
        'pand_kolom_class': pand_kolom_class,
    }
    return render(request, 'panden/index.html', context)


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'pand': pand
    }
    return render(request, 'panden/pand_detail.html', context)