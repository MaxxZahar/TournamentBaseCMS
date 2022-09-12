from modeltranslation.translator import TranslationOptions, register
from ..models import PlayerCardPage


@register(PlayerCardPage)
class PlayerCardPageTranslationOptions(TranslationOptions):
    pass
