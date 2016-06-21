from modeltranslation.translator import translator, TranslationOptions
from .models import Stavaza, DossierDocStatus, DossierDocBeschrijving


# Velden die vertaald moeten worden voor Stavaza
class StavazaTranslationOptions(TranslationOptions):
    fields = ('status',)


# Velden die vertaald moeten worden voor DossierDocStatus
class DossierDocStatusTranslationOptions(TranslationOptions):
    fields = ('status',)


# Velden die vertaald moeten worden voor DossierDocBeschrijving
class DossierDocBeschrijvingTranslationOptions(TranslationOptions):
    fields = ('dossier_naam',)

translator.register(Stavaza, StavazaTranslationOptions)
translator.register(DossierDocStatus, DossierDocStatusTranslationOptions)
translator.register(DossierDocBeschrijving, DossierDocBeschrijvingTranslationOptions)
