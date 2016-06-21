from dal import autocomplete
from django import forms

from gebruikers.models import Gebruiker


# Formulier voor autocomplete van gebruikers in adminpaneel
class GebruikerForm(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = '__all__'
        widgets = {
            'adres': autocomplete.ModelSelect2(url='adres-autocomplete')
        }


# Formulier voor autocomplete van woonplaatsen en landen bij adres in adminpaneel
class AdresForm(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = '__all__'
        widgets = {
            'woonplaats': autocomplete.ModelSelect2(url='woonplaats-autocomplete'),
            'land': autocomplete.ModelSelect2(url='land-autocomplete')
        }
