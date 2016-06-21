from modeltranslation.translator import translator, TranslationOptions
from .models import Land, Woonplaats


# Velden om vertaalbaar te maken bij Land
class LandTranslationOptions(TranslationOptions):
    fields = ('naam',)


# Velden om vertaalbaar te maken bij Woonplaats
class WoonplaatsTranslationOptions(TranslationOptions):
    fields = ('gemeente',)

translator.register(Land, LandTranslationOptions)
translator.register(Woonplaats, WoonplaatsTranslationOptions)
