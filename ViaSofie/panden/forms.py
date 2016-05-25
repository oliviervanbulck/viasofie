from dal import autocomplete
from django import forms

from ViaSofie.functions import get_alle_gemeentes
from dossiers.models import StavazaLijn, DossierDocLijn
from panden.models import Type, Pand, PandKenmerkPerPand


class AdvancedSearchForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('eender', 'Eender')]

    # De gemeentes & soorten moeten in een bepaald formaat!
    GEMEENTES = [('', 'Eender')] + [(gemeente.gemeente, gemeente.gemeente) for gemeente in get_alle_gemeentes()]
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


# Fix om ervoor te zorgen dat een inline sowieso wordt aangemaakt.
class AlwaysChangedModelForm(forms.ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial.
        By always returning true even unchanged inlines will get validated and saved."""
        return True


class PandForm(forms.ModelForm):
    class Meta:
        model = Pand
        fields = '__all__'
        widgets = {
            'type': autocomplete.ModelSelect2(url='type-autocomplete'),
            'adres': autocomplete.ModelSelect2(url='adres-autocomplete')
        }


class PandKenmerkPerPandForm(AlwaysChangedModelForm):
    class Meta:
        model = PandKenmerkPerPand
        fields = '__all__'
        widgets = {
            'kenmerk': autocomplete.ModelSelect2(url='pandkenmerk-autocomplete')
        }


class StavazaLijnForm(forms.ModelForm):
    class Meta:
        model = StavazaLijn
        fields = '__all__'
        widgets = {
            'stavaza': autocomplete.ModelSelect2(url='stavaza-autocomplete')
        }


class DossierDocLijnForm(forms.ModelForm):
    class Meta:
        model = DossierDocLijn
        fields = '__all__'
        widgets = {
            'beschrijving': autocomplete.ModelSelect2(url='dossierdoc-autocomplete')
        }
