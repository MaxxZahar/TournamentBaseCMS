from django.db import models
from garpix_page.models import BaseListPage


class TournamentPage(BaseListPage):
    paginate_by = 25
    template = 'pages/tournament.html'

    class Meta:
        verbose_name = "Турниры"
        verbose_name_plural = "Турниры"
        ordering = ('-created_at',)
