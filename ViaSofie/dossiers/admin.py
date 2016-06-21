from django.contrib import admin

# Register your models here.

from dossiers.models import StavazaLijn, Stavaza, DossierDocLijn, DossierDocStatus, DossierDocBeschrijving


# Basis ModelAdmin voor AdminModel objecten die niet zichtbaar mogen zijn op indexpagina van adminpaneel.
class HiddenAdminModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# StavazaLijn niet laten weergeven in adminpaneel
class StavazaLijnAdmin(HiddenAdminModel):
    pass


# Stavaza niet laten weergeven in adminpaneel
class StavazaAdmin(HiddenAdminModel):
    pass


# DossierDocLijn niet laten weergeven in adminpaneel
class DossierDocLijnAdmin(HiddenAdminModel):
    pass


# DossierDocStatus niet laten weergeven in adminpaneel
class DossierDocStatusAdmin(HiddenAdminModel):
    pass


# DossierDocBeschrijving niet laten weergeven in adminpaneel
class DossierDocBeschrijvingAdmin(HiddenAdminModel):
    pass


admin.site.register(StavazaLijn, StavazaLijnAdmin)
admin.site.register(Stavaza, StavazaAdmin)
admin.site.register(DossierDocLijn, DossierDocLijnAdmin)
admin.site.register(DossierDocStatus, DossierDocStatusAdmin)
admin.site.register(DossierDocBeschrijving, DossierDocBeschrijvingAdmin)
