from django import forms
from ViaSofie.functions import get_alle_gemeentes
from panden.models import Type


class NameForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('eender', 'Eender')]

    # De gemeentes & soorten moeten in een bepaald formaat!
    GEMEENTES = [(gemeente, gemeente) for gemeente in get_alle_gemeentes()]
    SOORTEN = [(soort, soort) for soort in Type.objects.all()]

    gemeente = forms.ChoiceField(choices=GEMEENTES, label='Gemeentes', required=True)
    soort = forms.ChoiceField(choices=SOORTEN, label='Soorten', required=True)
    zwembad = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Zwembad', required=True, initial='eender')
    tuin = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Tuin', required=True, initial='eender')
