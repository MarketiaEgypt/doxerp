from modeltranslation.translator import TranslationOptions, translator

from settings.models import Setting, Contact, ClientLogo


class SettingTranslationOptions(TranslationOptions):
    fields = ('site_name',  'address', 'description','description_footer','meta_title', 'meta_description', 'keywords')


class ClientLogoTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Setting, SettingTranslationOptions)
translator.register(ClientLogo, ClientLogoTranslationOptions)
