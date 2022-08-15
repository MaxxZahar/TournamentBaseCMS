from django.db import models
from garpix_page.models import BaseListPage


class PlayersPage(BaseListPage):
    paginate_by = 12
    template = 'pages/players.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import PlayerModel
        from ..serializers import PlayerSerializer
        from ..utilities import paginate, get_page
        context = super().get_context(request, *args, **kwargs)
        queryset = PlayerModel.objects.all()
        pages = paginate(queryset, self.paginate_by)
        page = get_page(pages, request)
        queryset = page.get('queryset')
        page_number = page.get('page_number')
        page_range = list(range(1, len(pages) + 1))
        players = PlayerSerializer(queryset, many=True).data
        total = PlayerModel.objects.all().count()
        context.update({
            'players': players,
            'page': page_number,
            'page_range': page_range,
            'total': total,
        })
        return context

    class Meta:
        verbose_name = "Игроки"
        verbose_name_plural = "Игроки"
        ordering = ('-created_at',)
