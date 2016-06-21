from modeltranslation.translator import translator, TranslationOptions
from .models import FaqItem


# Bepaal velden die vertaald moeten kunnen worden
class FaqItemTranslationOptions(TranslationOptions):
    fields = ('titel', 'tekst',)

translator.register(FaqItem, FaqItemTranslationOptions)
