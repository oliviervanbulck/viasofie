from modeltranslation.translator import translator, TranslationOptions
from .models import Stavaza, DossierDocStatus, DossierDocBeschrijving


class StavazaTranslationOptions(TranslationOptions):
    fields = ('status',)


class DossierDocStatusTranslationOptions(TranslationOptions):
    fields = ('status',)


class DossierDocBeschrijvingTranslationOptions(TranslationOptions):
    fields = ('dossier_naam',)

translator.register(Stavaza, StavazaTranslationOptions)
translator.register(DossierDocStatus, DossierDocStatusTranslationOptions)
translator.register(DossierDocBeschrijving, DossierDocBeschrijvingTranslationOptions)
