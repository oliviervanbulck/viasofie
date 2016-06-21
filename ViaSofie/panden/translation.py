from modeltranslation.translator import translator, TranslationOptions
from .models import Pand, Kenmerk, Type


# Velden om te vertalen bij Panden
class PandTranslationOptions(TranslationOptions):
    fields = ('algemene_beschrijving',)


# Velden om te vertalen bij Kenmerken
class KenmerkTranslationOptions(TranslationOptions):
    fields = ('benaming',)


# Velden om te vertalen bij Types
class TypeTranslationOptions(TranslationOptions):
    fields = ('type',)

translator.register(Pand, PandTranslationOptions)
translator.register(Kenmerk, KenmerkTranslationOptions)
translator.register(Type, TypeTranslationOptions)
