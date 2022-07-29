from django.db import models
from garpix_page.models import BaseListPage


class TournamentPage(BaseListPage):
    paginate_by = 25
    template = 'pages/tournament.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import TournamentModel
        from ..serializers import TournamentSerializer
        context = super().get_context(request, *args, **kwargs)
        tournaments = TournamentSerializer(TournamentModel.objects.all(), many=True).data
        context.update({
            'tournaments': tournaments,
        })
        return context

    class Meta:
        verbose_name = "Турниры"
        verbose_name_plural = "Турниры"
        ordering = ('-created_at',)
