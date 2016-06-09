from modeltranslation.translator import translator, TranslationOptions
from .models import Kenmerk


class KenmerkTranslationOptions(TranslationOptions):
    fields = ('benaming',)

translator.register(Kenmerk, KenmerkTranslationOptions)
