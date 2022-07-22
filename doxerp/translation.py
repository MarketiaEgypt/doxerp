from modeltranslation.translator import TranslationOptions, translator

from doxerp.models import Services, Solutions


class ServicesTranslationOptions(TranslationOptions):
    fields = ('name','description','meta_title', 'meta_description', 'keywords')


class SolutionsTranslationOptions(TranslationOptions):
    fields = ('name','description')


translator.register(Services, ServicesTranslationOptions)
translator.register(Solutions, SolutionsTranslationOptions)
