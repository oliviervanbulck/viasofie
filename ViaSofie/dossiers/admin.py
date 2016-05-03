from django.contrib import admin

# Register your models here.

from dossiers.models import Dossier, StavazaLijn, Stavaza, DossierDocLijn, DossierDocStatus, DossierDocBeschrijving


admin.site.register(Dossier)
admin.site.register(StavazaLijn)
admin.site.register(Stavaza)
admin.site.register(DossierDocLijn)
admin.site.register(DossierDocStatus)
admin.site.register(DossierDocBeschrijving)
