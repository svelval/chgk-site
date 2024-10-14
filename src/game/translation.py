from .models import Season, Group, Game
from modeltranslation.translator import TranslationOptions, register


@register(Season)
class SeasonTranslation(TranslationOptions):
    fields = ('rules', )


@register(Group)
class GroupTranslation(TranslationOptions):
    fields = ('name',)


@register(Game)
class GameTranslation(TranslationOptions):
    fields = ('full_name',)
