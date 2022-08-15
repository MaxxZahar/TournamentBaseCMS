from django.db import models
from garpix_page.models import BaseListPage


class TournamentPage(BaseListPage):
    paginate_by = 25
    template = 'pages/tournament.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import TournamentModel
        from ..serializers import TournamentSerializer
        from ..utilities import paginate, get_page
        context = super().get_context(request, *args, **kwargs)
        queryset = TournamentModel.objects.all()
        pages = paginate(queryset, self.paginate_by)
        page = get_page(pages, request)
        queryset = page.get('queryset')
        page_number = page.get('page_number')
        page_range = list(range(1, len(pages) + 1))
        tournaments = TournamentSerializer(queryset, many=True).data
        context.update({
            'tournaments': tournaments,
            'page': page_number,
            'page_range': page_range,
        })
        return context

    class Meta:
        verbose_name = "Турниры"
        verbose_name_plural = "Турниры"
        ordering = ('-created_at',)
