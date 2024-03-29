from dal import autocomplete
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.shortcuts import render
from django.shortcuts import redirect
from ViaSofie.functions import get_alle_actieve_panden
from ViaSofie.functions import get_alle_gemeentes
from ViaSofie.functions import keyword_search
from ViaSofie.functions import advanced_search
from dossiers.models import Stavaza, DossierDocBeschrijving
from gebruikers.models import Adres
from .models import Pand, Kenmerk, Hit
from .models import Type
from .forms import AdvancedSearchForm
from ViaSofie.templatetags.viasofie_filters import in_euro, in_opp
from django.utils.translation import get_language


# Overzicht van panden voor zowel huren als kopen
def panden_general(request, nbar_val):
    def check_get_parameters():
        required_params = ['prijs_upper', 'prijs_lower', 'gemeente', 'oppervlakte_upper', 'oppervlakte_lower',
                           'type', 'slaapkamer_lower', 'badkamer_lower', 'parking', 'terras', 'tuin',
                           'bemeubeld', 'bouwjaar']
        for param in required_params:
            if param not in request.GET:
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

    if request.GET and request.GET.get('search') and ('clearPanden' not in request.GET):
        panden = keyword_search(Pand, request.GET['search'],
                                ('adres__straat', 'adres__woonplaats__gemeente', 'adres__woonplaats__postcode',
                                 'adres__huisnummer', 'type__type_' + get_language(),))
        context['search'] = request.GET['search']
    elif check_get_parameters():
        # Make sure the form doesn't reset
        context['form'] = AdvancedSearchForm(request.GET)

        # Filter op de juiste panden
        panden = advanced_search(request)
    else:
        panden = get_alle_actieve_panden()

    paginator = Paginator(panden, 12)  # Toon 12 panden per pagina

    page = request.GET.get('page')
    try:
        panden = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        panden = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        panden = paginator.page(paginator.num_pages)

    context['pand_kolom_class'] = 'col-lg-4 col-md-6'
    context['panden'] = panden
    context['paginator'] = paginator

    return render(request, 'panden/index.html', context)


# Overzicht panden kopen
def index(request):
    return panden_general(request, 'kopen')


# Overzicht panden huren
def huren(request):
    return panden_general(request, 'huren')


# Detailweergave van een pand
def pand_detail(request, pand_id):
    pand = Pand.objects.get(id=pand_id)

    # Indien een pand inactief is moet het niet getoond worden
    if not pand.actief:
        return redirect('panden.index')

    check = Hit.objects.filter(pand_id__exact=pand.id, session=request.session.session_key).count()
    if check == 0:
        new_hit = Hit(pand=pand, session=request.session.session_key)
        new_hit.save()

    hits = Hit.objects.filter(pand_id=pand.id).count()

    context = {
        'maps_adres': pand.adres,
        'basis_kenmerken': [(pand.adres, 'Adres'), (in_euro(pand.prijs), 'Prijs'), (pand.type, 'Type'),
                            (pand.bouwjaar, 'Bouwjaar'), (in_opp(pand.oppervlakte), 'Oppervlakte'),
                            (pand.algemene_beschrijving, 'Beschrijving')],
        'kenmerken': pand.pandkenmerkperpand_set.all().order_by('kenmerk__benaming'),
        'fotos': pand.foto_set.all(),
        'links': pand.pandimmolink_set.all(),
        'pand': pand,
        'prev_url': request.META.get('HTTP_REFERER', None),
        'hits': hits,
    }
    context.update({'nbar': 'kopen'})
    return render(request, "panden/pand_detail.html", context)


# Autocomplete voor Type in adminpaneel
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


# Autocomplete voor Adres in adminpaneel
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


# Autocomplete voor Pandkenmerk in adminpaneel
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


# Autocomplete voor Stavaza in adminpaneel
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


# Autocomplete voor Dossierdoc in adminpaneel
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
