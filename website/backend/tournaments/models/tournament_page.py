from django.db import models
from garpix_page.models import BaseListPage


class TournamentPage(BaseListPage):
    paginate_by = 25
    template = 'pages/tournament.html'

    def get_context(self, request=None, *args, **kwargs):
        from django.db.models import Count
        from ..models import TournamentModel
        from ..serializers import TournamentSerializer
        from ..utilities import paginate, get_page
        context = super().get_context(request, *args, **kwargs)
        queryset = TournamentModel.objects.all()
        queryset = queryset.annotate(number_of_games=Count('tournament', distinct=True)).\
            annotate(number_of_players=Count('tournament_players', distinct=True))
        par = request.GET.get('ordering', False)
        ordering_set = {'name', 'location', 'finish_date', 'number_of_players', 'number_of_games'}
        ordering_set_reverse = {'-' + item for item in ordering_set}
        if par in ordering_set.union(ordering_set_reverse):
            queryset = queryset.order_by(par)
        pages = paginate(queryset, self.paginate_by)
        page = get_page(pages, request)
        queryset = page.get('queryset')
        page_number = page.get('page_number')
        page_range = list(range(1, len(pages) + 1))
        tournaments = TournamentSerializer(queryset, many=True).data
        total = TournamentModel.objects.all().count()
        context.update({
            'tournaments': tournaments,
            'page': page_number,
            'page_range': page_range,
            'total': total,
        })
        return context

    class Meta:
        verbose_name = "Турниры"
        verbose_name_plural = "Турниры"
        ordering = ('-created_at',)
