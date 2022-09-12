from ..models.player_card_page import PlayerCardPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PlayerCardPage)
class PlayerCardPageAdmin(BasePageAdmin):
    pass
