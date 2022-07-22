from django.db import models
from garpix_page.models import BaseListPage


class PlayersPage(BaseListPage):
    paginate_by = 25
    template = 'pages/players.html'

    class Meta:
        verbose_name = "Игроки"
        verbose_name_plural = "Игроки"
        ordering = ('-created_at',)
