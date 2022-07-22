from modeltranslation.translator import TranslationOptions, register
from ..models import PlayersPage


@register(PlayersPage)
class PlayersPageTranslationOptions(TranslationOptions):
    pass
