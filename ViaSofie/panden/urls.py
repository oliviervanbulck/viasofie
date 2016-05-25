from django.conf.urls import url

from panden.views import TypeAutocomplete, AdresAutocomplete, PandkenmerkAutocomplete, StavazaAutocomplete, \
    DossierdocAutocomplete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='panden.index'),
    url(r'^kopen/$', views.index, name='panden.kopen'),
    url(r'^huren/$', views.huren, name='panden.huren'),
    url(r'^(?P<pand_id>[0-9]+)$', views.pand_detail, name='panden.detail'),
    url(
        r'^type-autocomplete/$',
        TypeAutocomplete.as_view(),
        name='type-autocomplete',
    ),
    url(
        r'^adres-autocomplete/$',
        AdresAutocomplete.as_view(),
        name='adres-autocomplete',
    ),
    url(
        r'^pandkenmerk-autocomplete/$',
        PandkenmerkAutocomplete.as_view(),
        name='pandkenmerk-autocomplete',
    ),
    url(
        r'^stavaza-autocomplete/$',
        StavazaAutocomplete.as_view(),
        name='stavaza-autocomplete',
    ),
    url(
        r'^dossierdoc-autocomplete/$',
        DossierdocAutocomplete.as_view(),
        name='dossierdoc-autocomplete',
    ),
]
