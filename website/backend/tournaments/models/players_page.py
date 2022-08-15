from django.db import models
from garpix_page.models import BaseListPage


class PlayersPage(BaseListPage):
    paginate_by = 12
    template = 'pages/players.html'

    def get_context(self, request=None, *args, **kwargs):
        from ..models import PlayerModel
        from ..serializers import PlayerSerializer
        context = super().get_context(request, *args, **kwargs)
        queryset = PlayerModel.objects.all()
        pages = paginate(queryset, self.paginate_by)
        page_number = 1
        page = get_page(pages, request)
        queryset = page['queryset']
        page_number = page['page_number']
        page_range = list(range(1, len(pages) + 1))
        players = PlayerSerializer(queryset, many=True).data
        context.update({
            'players': players,
            'page': page_number,
            'page_range': page_range,
        })
        return context

    class Meta:
        verbose_name = "Игроки"
        verbose_name_plural = "Игроки"
        ordering = ('-created_at',)


def paginate(queryset, paginate_by):
    total = len(queryset)
    pages = []
    i = 0
    j = 0
    data = []
    page = {}
    number = 1
    for item in queryset:
        data.append(item)
        i += 1
        j += 1
        if i == paginate_by:
            i = 0
            page['data'] = data
            page['number'] = number
            number += 1
            pages.append(page)
            page = {}
            data = []
        elif j == total:
            page['data'] = data
            page['number'] = number
            pages.append(page)
    return pages


def get_page(pages, request):
    if request.GET.get('page', False):
        try:
            page_number = int(request.GET.get('page'))
            if page_number > len(pages) or page_number < 1:
                raise ValueError
        except ValueError:
            print('Wrong request')
        queryset = pages[page_number - 1]['data']
    else:
        queryset = pages[0]['data']
    return {
        'queryset': queryset,
        'page_number': page_number
    }
