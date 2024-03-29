from dal import autocomplete
from django import forms
from datetime import date

from ViaSofie.functions import get_alle_gemeentes
from dossiers.models import StavazaLijn, DossierDocLijn
from panden.models import Type, Pand, PandKenmerkPerPand


# Formulier voor Advanced Search
class AdvancedSearchForm(forms.Form):
    # When migrating this form is loaded but its tables don't exist yet, so a try block will prevent that crash.
    try:
        KEUZES = [('ja', 'Ja'),
                  ('nee', 'Nee'),
                  ('nvt', 'N.v.t.')]

        # Prijs: Textboxen voor slider (lower / upper limit)
        prijs_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-lower-value', 'readonly': True, 'size': 10, 'class': 'hidden-box formatted'}), label='Min', initial=50000)
        prijs_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'prijs-upper-value', 'readonly': True, 'size': 10, 'class': 'hidden-box formatted'}), label='Max', initial=1000000)

        # Gemeente: Dropdownmenu
        GEMEENTES = [KEUZES[-1]] + [(gemeente.gemeente, gemeente.gemeente) for gemeente in get_alle_gemeentes()]
        gemeente = forms.ChoiceField(choices=GEMEENTES, label='Gemeentes', required=True)

        # Oppervlakte: Textboxen voor slider (lower / upper limit)
        oppervlakte_lower = forms.CharField(widget=forms.TextInput(attrs={'id': 'oppervlakte-lower-value', 'readonly': True, 'size': 10, 'class': 'hidden-box'}), label='Min', initial=150)
        oppervlakte_upper = forms.CharField(widget=forms.TextInput(attrs={'id': 'oppervlakte-upper-value', 'readonly': True, 'size': 10, 'class': 'hidden-box'}), label='Max', initial=300)

        # Type: Dropdownmenu
        TYPES = [KEUZES[-1]] + [(type, type) for type in Type.objects.all()]
        type = forms.ChoiceField(choices=TYPES, label='Types', required=True)

        # Slaapkamer: Textbox
        slaapkamer_lower = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}), label='Minimum aantal slaapkamers:', initial="2")

        # Badkamer: Textbox
        badkamer_lower = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}), label='Minimum aantal badkamers:', initial="1")

        # Parking/Garage: Checkbox
        parking = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Parking / Garage:', required=True, initial=KEUZES[-1][0])

        # Terras: Checkbox
        terras = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Terras:', required=True, initial=KEUZES[-1][0])

        # Tuin: Checkbox
        tuin = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Tuin:', required=True, initial=KEUZES[-1][0])

        # Bemeubeld: Checkbox
        bemeubeld = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Bemeubeld:', required=True, initial=KEUZES[-1][0])

        # Bouwjaar: Textbox
        #bouwjaar = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}), label='Bouwjaar:', initial="2000")
        STARTJAAR = 1940
        STANDAARDJAAR = 2000
        BOUWJAREN = [(jaar, jaar) for jaar in range(STARTJAAR, date.today().year + 1)]
        bouwjaar = forms.ChoiceField(choices=BOUWJAREN, label='Bouwjaar', initial=STANDAARDJAAR)
    except:
        pass


# Fix om ervoor te zorgen dat een inline sowieso wordt aangemaakt.
class AlwaysChangedModelForm(forms.ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial.
        By always returning true even unchanged inlines will get validated and saved."""
        return True


# Formulier voor autocomplete in admin bij panden
class PandForm(forms.ModelForm):
    class Meta:
        model = Pand
        fields = '__all__'
        widgets = {
            'type': autocomplete.ModelSelect2(url='type-autocomplete'),
            'adres': autocomplete.ModelSelect2(url='adres-autocomplete')
        }


# Formulier voor autocomplete in admin bij pandkenmerkenperpand
class PandKenmerkPerPandForm(AlwaysChangedModelForm):
    class Meta:
        model = PandKenmerkPerPand
        fields = '__all__'
        widgets = {
            'kenmerk': autocomplete.ModelSelect2(url='pandkenmerk-autocomplete')
        }


# Formulier voor autocomplete in admin bij stavazalijnen
class StavazaLijnForm(forms.ModelForm):
    class Meta:
        model = StavazaLijn
        fields = '__all__'
        widgets = {
            'stavaza': autocomplete.ModelSelect2(url='stavaza-autocomplete')
        }


# Formulier voor autocomplete in admin bij dossierdoclijnen
class DossierDocLijnForm(forms.ModelForm):
    class Meta:
        model = DossierDocLijn
        fields = '__all__'
        widgets = {
            'beschrijving': autocomplete.ModelSelect2(url='dossierdoc-autocomplete')
        }

