from modeltranslation.translator import translator, TranslationOptions
from .models import Pand, Kenmerk


class PandTranslationOptions(TranslationOptions):
    fields = ('algemene_beschrijving',)


class KenmerkTranslationOptions(TranslationOptions):
    fields = ('benaming',)

translator.register(Pand, PandTranslationOptions)
translator.register(Kenmerk, KenmerkTranslationOptions)
