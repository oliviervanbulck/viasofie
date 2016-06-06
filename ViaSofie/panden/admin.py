from django.contrib import admin

# Register your models here.
from ViaSofie.templatetags.viasofie_filters import in_euro
from dossiers.models import StavazaLijn, DossierDocLijn
from panden.forms import PandKenmerkPerPandForm, StavazaLijnForm, DossierDocLijnForm, PandForm
from panden.models import Pand, Type, Kenmerk, PandImmoLink, Foto, PandKenmerkPerPand, CarouselFoto, KenmerkType, Switch, \
    ImmoSite
from django.forms.models import ModelForm


# Basis ModelAdmin voor AdminModel objecten die niet zichtbaar mogen zijn op indexpagina van adminpaneel.
class HiddenAdminModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# Fix om ervoor te zorgen dat een inline sowieso wordt aangemaakt.
class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial.
        By always returning true even unchanged inlines will get validated and saved."""
        return True


"""
Filters
"""


class PandFotoFilter(admin.SimpleListFilter):
    title = 'Pand'
    parameter_name = 'pand'

    def lookups(self, request, model_admin):
        panden = Pand.objects.filter(dossier__actief=True)
        return [(p.id, p.__str__) for p in panden]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(pand__id__exact=self.value())
        else:
            return queryset


"""
Inlines
"""


class StavazaLijnenInline(admin.TabularInline):
    model = StavazaLijn
    form = StavazaLijnForm
    can_delete = True
    extra = 0
    verbose_name_plural = 'Actuele statussen'
    verbose_name = 'Actuele status'
    fields = ('stavaza', 'datum',)


class DocLijnenInline(admin.TabularInline):
    model = DossierDocLijn
    form = DossierDocLijnForm
    can_delete = True
    extra = 0
    verbose_name_plural = 'Dossierinhoud'
    verbose_name = 'Dossierinhoud'


class PandKenmerkPerPandInline(admin.TabularInline):
    model = PandKenmerkPerPand
    form = PandKenmerkPerPandForm
    can_delete = True
    verbose_name_plural = 'Pandkenmerken'
    extra = 0
    fields = ('kenmerk', 'aantal',)


class PandImmoLinkInline(admin.TabularInline):
    model = PandImmoLink
    can_delete = True
    verbose_name_plural = 'Links'
    form = AlwaysChangedModelForm
    extra = 0


class FotoInline(admin.TabularInline):
    model = Foto
    can_delete = True
    verbose_name_plural = 'Foto\'s'
    form = AlwaysChangedModelForm
    fields = ('pand_foto', 'foto',)
    readonly_fields = ('pand_foto',)
    extra = 0

    def pand_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    pand_foto.allow_tags = True
    pand_foto.short_description = 'Voorbeeld'


"""
AdminModels - Hidden
"""


class FotoAdmin(HiddenAdminModel):
    pass


class KenmerkAdmin(HiddenAdminModel):
    pass


class PandKenmerkPerPandAdmin(HiddenAdminModel):
    pass


class PandImmoLinkAdmin(HiddenAdminModel):
    pass


class TypeAdmin(HiddenAdminModel):
    pass


class KenmerkTypeAdmin(HiddenAdminModel):
    pass


"""
AdminModels - Shown
"""


class CarouselFotoAdmin(admin.ModelAdmin):
    list_display = ('carousel_foto', 'actief',)
    list_per_page = 10
    readonly_fields = ('carousel_foto',)
    actions = ['set_active', 'set_inactive']

    def carousel_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    def set_active(self, request, queryset):
        queryset.update(actief=True)

    set_active.short_description = 'Maak slides actief'

    def set_inactive(self, request, queryset):
        queryset.update(actief=False)

    set_inactive.short_description = 'Maak slides inactief'

    carousel_foto.allow_tags = True
    carousel_foto.short_description = 'Foto'


class PandAdmin(admin.ModelAdmin):
    inlines = (PandKenmerkPerPandInline, PandImmoLinkInline, FotoInline, StavazaLijnenInline, DocLijnenInline)
    search_fields = ('adres__straat', 'adres__woonplaats__gemeente', 'adres__woonplaats__postcode', 'adres__huisnummer', 'type__type',)
    list_filter = ('type', 'bouwjaar', 'adres__land',)
    readonly_fields = ('qr_code',)
    exclude = ('qrcode',)
    form = PandForm
    actions = ('set_active', 'set_inactive',)
    list_display = ('adres', 'type', 'get_prijs_format', 'actief',)
    list_per_page = 25

    def qr_code(self, obj):
        return '<img src="%s" />' % obj.qrcode.url

    def get_prijs_format(self, obj):
        return in_euro(obj.prijs)

    get_prijs_format.short_description = 'Prijs'

    def set_active(self, request, queryset):
        queryset.update(actief=True)

    set_active.short_description = 'Maak panden actief'

    def set_inactive(self, request, queryset):
        queryset.update(actief=False)

    set_inactive.short_description = 'Maak panden inactief'

    qr_code.allow_tags = True
    qr_code.short_description = "QR code"

admin.site.register(Pand, PandAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Kenmerk, KenmerkAdmin)
admin.site.register(PandImmoLink, PandImmoLinkAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(CarouselFoto, CarouselFotoAdmin)
admin.site.register(PandKenmerkPerPand, PandKenmerkPerPandAdmin)
admin.site.register(KenmerkType, KenmerkTypeAdmin)
admin.site.register(ImmoSite)
admin.site.register(Switch)
