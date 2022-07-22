from modeltranslation.translator import TranslationOptions, translator

from blog.models import Category, Post, Tag


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


class PostTranslationOptions(TranslationOptions):
    fields = ('author', 'title', 'description_one', 'description_two',)


translator.register(Post, PostTranslationOptions)

translator.register(Tag, TagTranslationOptions)

translator.register(Category, CategoryTranslationOptions)