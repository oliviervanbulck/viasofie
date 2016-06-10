from modeltranslation.translator import translator, TranslationOptions
from .models import Pand, Kenmerk, Type


class PandTranslationOptions(TranslationOptions):
    fields = ('algemene_beschrijving',)


class KenmerkTranslationOptions(TranslationOptions):
    fields = ('benaming',)


class TypeTranslationOptions(TranslationOptions):
    fields = ('type',)

translator.register(Pand, PandTranslationOptions)
translator.register(Kenmerk, KenmerkTranslationOptions)
translator.register(Type, TypeTranslationOptions)
