from dal import autocomplete
from django import forms

from ViaSofie.functions import get_alle_gemeentes
from dossiers.models import StavazaLijn, DossierDocLijn
from panden.models import Type, Pand, PandKenmerkPerPand


class AdvancedSearchForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('nvt', 'nvt')]

    # Prijs: Textboxen voor slider (lower / upper limit)
    prijs_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-lower-value'}), label='Min')
    prijs_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-upper-value'}), label='Max')

    # Gemeente: Dropdownmenu
    GEMEENTES = [('nvt', 'n.v.t.')] + [(gemeente.gemeente, gemeente.gemeente) for gemeente in get_alle_gemeentes()]
    gemeente = forms.ChoiceField(choices=GEMEENTES, label='Gemeentes', required=True)

    # Oppervlakte: Textboxen voor slider (lower / upper limit)
    oppervlakte_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'oppervlakte-lower-value'}), label='Min')
    oppervlakte_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'oppervlakte-upper-value'}), label='Max')

    # Type: Dropdownmenu
    TYPES = [('nvt', 'n.v.t.')] + [(type, type) for type in Type.objects.all()]
    type = forms.ChoiceField(choices=TYPES, label='Types', required=True)

    # Slaapkamer: Textbox
    slaapkamer_lower = forms.CharField(widget=forms.TextInput(), label='Minimum aantal slaapkamers:')

    # Badkamer: Textbox
    badkamer_lower = forms.CharField(widget=forms.TextInput(), label='Minimum aantal badkamers:')

    # Parking/Garage: Checkbox
    parking = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Parking / Garage:', required=True, initial='n.v.t.')

    # Terras: Checkbox
    terras = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Terras:', required=True, initial='n.v.t.')

    # Tuin: Checkbox
    tuin = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Tuin:', required=True, initial='n.v.t.')

    # Bemeubeld: Checkbox
    bemeubeld = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Bemeubeld:', required=True, initial='n.v.t.')

    # Bouwjaar: Textbox
    bouwjaar = forms.CharField(widget=forms.TextInput(), label='Bouwjaar:')


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

