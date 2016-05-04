from django.contrib import admin

# Register your models here.

from dossiers.models import Dossier, StavazaLijn, Stavaza, DossierDocLijn, DossierDocStatus, DossierDocBeschrijving


# Basis ModelAdmin voor AdminModel objecten die niet zichtbaar mogen zijn op indexpagina van adminpaneel.
class HiddenAdminModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DossierDocLijnInline(admin.TabularInline):
    model = DossierDocLijn
    can_delete = True
    extra = 0
    verbose_name_plural = 'Documenten'
    verbose_name = 'Document'


class StavazaLijnInline(admin.TabularInline):
    model = StavazaLijn
    can_delete = True
    extra = 0
    verbose_name_plural = 'Stavaza'
    verbose_name = 'Stand van zaken'


class DossierAdmin(HiddenAdminModel):
    fields = ('terug_naar_pand', 'actief',)
    readonly_fields = ('terug_naar_pand',)
    inlines = (DossierDocLijnInline, StavazaLijnInline,)

    def terug_naar_pand(self, obj):
        return '<a href="/admin/panden/pand/%d/change/">Terug naar pand</a>' % obj.pand.id

    terug_naar_pand.allow_tags = True
    terug_naar_pand.short_description = ''


class StavazaLijnAdmin(HiddenAdminModel):
    pass


class StavazaAdmin(HiddenAdminModel):
    pass


class DossierDocLijnAdmin(HiddenAdminModel):
    pass


class DossierDocStatusAdmin(HiddenAdminModel):
    pass


class DossierDocBeschrijvingAdmin(HiddenAdminModel):
    pass


admin.site.register(Dossier, DossierAdmin)
admin.site.register(StavazaLijn, StavazaLijnAdmin)
admin.site.register(Stavaza, StavazaAdmin)
admin.site.register(DossierDocLijn, DossierDocLijnAdmin)
admin.site.register(DossierDocStatus, DossierDocStatusAdmin)
admin.site.register(DossierDocBeschrijving, DossierDocBeschrijvingAdmin)
