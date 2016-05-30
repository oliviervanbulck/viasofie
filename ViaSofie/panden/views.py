from dal import autocomplete
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.shortcuts import render
from ViaSofie.functions import get_alle_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from ViaSofie.functions import keyword_search
from ViaSofie.functions import advanced_search
from dossiers.models import Stavaza, DossierDocBeschrijving
from gebruikers.models import Adres
from .models import Pand, Kenmerk
from .models import Type
from .forms import AdvancedSearchForm
from ViaSofie.templatetags.viasofie_filters import in_euro, in_opp


def panden_general(request, nbar_val):
    def check_get_parameters():
        required_params = ['prijs_upper', 'prijs_lower', 'gemeente', 'oppervlakte_upper', 'oppervlakte_lower',
                           'type', 'slaapkamer_lower', 'badkamer_lower', 'parking', 'terras', 'tuin',
                           'bemeubeld', 'bouwjaar']
        for param in required_params:
            if param not in request.GET:
                print param
                return False
        return True

    pand_types = Type.objects.all()
    gemeentes = get_alle_gemeentes()

    context = {
        'nbar': nbar_val,
        'pand_types': pand_types,
        'gemeentes': gemeentes,
        'form': AdvancedSearchForm()
    }

    if request.POST and request.POST['search'] and ('clearPanden' not in request.POST):
        panden = keyword_search(Pand, request.POST['search'],
                                ('adres__straat', 'adres__woonplaats__gemeente', 'adres__woonplaats__postcode', 'adres__huisnummer',
                                 'type__type',))
        context['search'] = request.POST['search']
    elif check_get_parameters():
        # Make sure the form doesn't reset
        context['form'] = AdvancedSearchForm(request.GET)

        # Filter op de juiste panden
        panden = advanced_search(request)
    else:
        panden = get_alle_actieve_panden()
    context['pand_kolom_class'] = 'col-lg-4 col-md-6'
    context['panden'] = panden

    return render(request, 'panden/index.html', context)


# Create your views here.
def index(request):
    return panden_general(request, 'kopen')


def huren(request):
    return panden_general(request, 'huren')


def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)
    context = {
        'maps_adres': pand.adres,
        'basis_kenmerken': [(pand.adres, 'Adres'), (in_euro(pand.prijs), 'Prijs'), (pand.type, 'Type'),
                            (pand.bouwjaar, 'Bouwjaar'), (in_opp(pand.oppervlakte), 'Oppervlakte')],
        'kenmerken': pand.pandkenmerkperpand_set.all().order_by('kenmerk__benaming'),
        'fotos': pand.foto_set.all(),
        'links': pand.pandimmolink_set.all(),
    }
    if request.method == 'GET':
        context.update({'nbar': 'kopen'})
        return render(request, "panden/pand_detail.html", context)


class TypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Type.objects.none()

        if not self.request.user.is_superuser:
            return Type.objects.none()

        qs = Type.objects.all()

        if self.q:
            qs = qs.filter(type__istartswith=self.q)

        return qs


class AdresAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Adres.objects.none()

        if not self.request.user.is_superuser:
            return Adres.objects.none()

        qs = Adres.objects.all()

        if self.q:
            qs = qs.annotate(volledig_adres=Concat('straat', V(' '), 'huisnummer', V(', '), 'woonplaats__postcode', V(' '), 'woonplaats__gemeente')).filter(volledig_adres__icontains=self.q)

        return qs


class PandkenmerkAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Kenmerk.objects.none()

        if not self.request.user.is_superuser:
            return Kenmerk.objects.none()

        qs = Kenmerk.objects.all()

        if self.q:
            qs = qs.filter(benaming__icontains=self.q)

        return qs


class StavazaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Stavaza.objects.none()

        if not self.request.user.is_superuser:
            return Stavaza.objects.none()

        qs = Stavaza.objects.all()

        if self.q:
            qs = qs.filter(status__icontains=self.q)

        return qs


class DossierdocAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return DossierDocBeschrijving.objects.none()

        if not self.request.user.is_superuser:
            return DossierDocBeschrijving.objects.none()

        qs = DossierDocBeschrijving.objects.all()

        if self.q:
            qs = qs.filter(dossier_naam__icontains=self.q)

        return qs
