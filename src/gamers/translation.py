from .models import Award, BasePlayer, Connoisseur, TVViewer
from modeltranslation.translator import TranslationOptions, register


@register(Award)
class AwardTranslation(TranslationOptions):
    fields = ('name', 'description', )


@register(BasePlayer)
class BasePlayerTranslation(TranslationOptions):
    fields = ('first_name', 'last_name', 'about', )


@register(Connoisseur)
class ConnoisseurTranslation(TranslationOptions):
    pass


@register(TVViewer)
class TVViewerTranslation(TranslationOptions):
    pass
