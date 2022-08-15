from django.db import models
from garpix_page.models import BaseListPage


class PlayersPage(BaseListPage):
    paginate_by = 25
    template = 'pages/players.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import PlayerModel
        from ..serializers import PlayerSerializer
        context = super().get_context(request, *args, **kwargs)
        players = PlayerSerializer(PlayerModel.objects.all(), many=True).data
        context.update({
            'players': players,
        })
        return context

    class Meta:
        verbose_name = "Игроки"
        verbose_name_plural = "Игроки"
        ordering = ('-created_at',)
