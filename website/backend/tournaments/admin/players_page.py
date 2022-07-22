from ..models.players_page import PlayersPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PlayersPage)
class PlayersPageAdmin(BasePageAdmin):
    pass
