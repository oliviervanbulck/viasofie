from django import forms
from ViaSofie.functions import get_alle_gemeentes
from panden.models import Type


class AdvancedSearchForm(forms.Form):
    KEUZES = [('ja', 'Ja'),
              ('nee', 'Nee'),
              ('nvt', 'nvt')]

    """Combinatie van alle filters
    panden = get_alle_actieve_panden()
    filters = [filter_prijs,
               filter_gemeente,
               filter_oppervlake,
               filter_type,
               filter_slaapkamers,
               filter_badkamers,
               filter_parking,
               filter_terras,
               filter_tuin,
               filter_bemeubeld,
               filter_bouwjaar]"""

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

    # Slaapkamers slider textboxes
    #slaapkamer_lower = forms.CharField(widget=forms.TextInput(), label='Min')

    # zwembad = forms.ChoiceField(choices=KEUZES, widget=forms.RadioSelect(), label='Zwembad', required=True, initial='n.v.t.')