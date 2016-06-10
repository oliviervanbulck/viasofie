from modeltranslation.translator import translator, TranslationOptions
from .models import FaqItem


class FaqItemTranslationOptions(TranslationOptions):
    fields = ('titel', 'tekst',)

translator.register(FaqItem, FaqItemTranslationOptions)
