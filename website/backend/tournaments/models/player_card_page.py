from django.db import models
from garpix_page.models import BasePage


class PlayerCardPage(BasePage):
    template = "pages/player_card.html"

    class Meta:
        verbose_name = "Профиль игрока"
        verbose_name_plural = "Профили игроков"
        ordering = ("-created_at",)
