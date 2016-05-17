from django import forms
from ViaSofie.functions import get_alle_gemeentes


class NameForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('eender', 'Eender')]

    # De gemeentes moeten in een bepaald formaat!
    GEMEENTES = []
    for gemeente in get_alle_gemeentes():
        GEMEENTES.append((gemeente, gemeente))

    gemeentes = forms.ChoiceField(choices=GEMEENTES)
    zwembad = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect())
    tuin = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect())
