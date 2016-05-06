from django.contrib import admin

# Register your models here.
from django.contrib.admin import SimpleListFilter
from django.contrib.contenttypes import forms

from dossiers.models import Dossier, StavazaLijn
from gebruikers.models import Adres
from panden.models import Pand, Type, Kenmerk, PandImmoLink, Foto, PandKenmerkPerPand, CarouselFoto
from django.forms.models import BaseInlineFormSet, ModelForm


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


class DossierInline(admin.TabularInline):
    model = Dossier
    can_delete = False
    verbose_name_plural = 'dossier'
    form = AlwaysChangedModelForm
    extra = 0
    fields = ('actief', 'get_admin_url',)
    readonly_fields = ('get_admin_url',)

    def get_admin_url(self, obj):
        return '<a href="/admin/dossiers/dossier/%s/change/" target="_blank">Wijzig dossier</a>' % str(obj.id)

    get_admin_url.allow_tags = True
    get_admin_url.short_description = 'Wijzig dossier'


class PandKenmerkPerPandInline(admin.TabularInline):
    model = PandKenmerkPerPand
    can_delete = True
    verbose_name_plural = 'Pandkenmerken'
    form = AlwaysChangedModelForm
    extra = 0


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


"""
AdminModels - Shown
"""


class CarouselFotoAdmin(admin.ModelAdmin):
    list_display = ('carousel_foto', 'actief',)
    list_per_page = 10
    readonly_fields = ('carousel_foto',)

    def carousel_foto(self, obj):
        return '<img src="%s" style="max-width: 150px;max-height:150px;" />' % obj.foto.url

    carousel_foto.allow_tags = True


class PandAdmin(admin.ModelAdmin):
    inlines = (DossierInline, PandKenmerkPerPandInline, PandImmoLinkInline, FotoInline,)
    raw_id_fields = ('gebruiker',)
    search_fields = ('adres__straat', 'adres__gemeente', 'adres__postcode', 'adres__huisnummer', 'type__type',)
    list_filter = ('type', 'bouwjaar', 'adres__land',)


admin.site.register(Pand, PandAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Kenmerk, KenmerkAdmin)
admin.site.register(PandImmoLink, PandImmoLinkAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(CarouselFoto, CarouselFotoAdmin)
admin.site.register(PandKenmerkPerPand, PandKenmerkPerPandAdmin)
