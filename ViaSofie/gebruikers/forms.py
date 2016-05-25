from dal import autocomplete
from django import forms

from gebruikers.models import Gebruiker


class GebruikerForm(forms.ModelForm):
    class Meta:
        model = Gebruiker
        fields = '__all__'
        widgets = {
            'adres': autocomplete.ModelSelect2(url='adres-autocomplete')
        }
