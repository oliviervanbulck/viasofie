from modeltranslation.translator import translator, TranslationOptions
from .models import Land, Woonplaats


class LandTranslationOptions(TranslationOptions):
    fields = ('naam',)


class WoonplaatsTranslationOptions(TranslationOptions):
    fields = ('gemeente',)

translator.register(Land, LandTranslationOptions)
translator.register(Woonplaats, WoonplaatsTranslationOptions)
