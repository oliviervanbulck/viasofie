from django import forms
from ViaSofie.functions import get_alle_gemeentes
from panden.models import Type


class AdvancedSearchForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('eender', 'Eender')]

    # De gemeentes & soorten moeten in een bepaald formaat!
    GEMEENTES = [('', 'Eender')] + [(gemeente, gemeente) for gemeente in get_alle_gemeentes()]
    SOORTEN = [('', 'Eender')] + [(soort, soort) for soort in Type.objects.all()]

    gemeente = forms.ChoiceField(choices=GEMEENTES, label='Gemeentes', required=True)
    soort = forms.ChoiceField(choices=SOORTEN, label='Soorten', required=True)
    zwembad = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Zwembad', required=True, initial='eender')
    tuin = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Tuin', required=True, initial='eender')

    # Slaapkamers slider textboxes
    slaapkamer_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'slaapkamers-lower-value'}), label='Min')
    slaapkamer_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'slaapkamers-upper-value'}), label='Max')

    # Prijs slider textboxes
    prijs_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-lower-value'}), label='Min')
    prijs_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-upper-value'}), label='Max')
