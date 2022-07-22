from modeltranslation.translator import TranslationOptions, register
from ..models import TournamentPage


@register(TournamentPage)
class TournamentPageTranslationOptions(TranslationOptions):
    pass
