from ..models.tournament_page import TournamentPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(TournamentPage)
class TournamentPageAdmin(BasePageAdmin):
    pass
