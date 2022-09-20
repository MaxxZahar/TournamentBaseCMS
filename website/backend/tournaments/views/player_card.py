from django.shortcuts import render, get_object_or_404
from ..models import PlayerModel, GameModel, SettingsModel
from django.db.models import Q
from ..utilities import frequency_dict, gain_opponents_list, paginate, get_page
from ..settings import NUMBER_OF_ITEMS_IN_LIST_OF_OPPONENTS, PLAYER_CARD_TOURNAMENTS_PER_PAGE


def player(request, player_id):
    if SettingsModel.objects.values():
        page_settings = SettingsModel.objects.values()[0]
    else:
        page_settings = {}
    player_ex = get_object_or_404(PlayerModel, pk=player_id)
    number_of_games = GameModel.objects.filter(player_1=player_ex).count() \
        + GameModel.objects.filter(player_2=player_ex).count()
    number_of_wins = GameModel.objects.filter(player_1=player_ex).filter(result='+').count() \
        + GameModel.objects.filter(player_2=player_ex).filter(result='-').count()
    winning_percentage = str("%.2f" % round(number_of_wins / number_of_games * 100, 2))
    q = GameModel.objects.filter(Q(player_1=player_ex) | Q(player_2=player_ex)).values('player_1', 'player_2', 'result')
    freq = frequency_dict(q, player_id)
    res = gain_opponents_list(freq, NUMBER_OF_ITEMS_IN_LIST_OF_OPPONENTS)
    if page_settings.get('number_of_opponents_in_pc'):
        res = gain_opponents_list(freq, page_settings['number_of_opponents_in_pc'])
    queryset = player_ex.get_tournaments()
    if page_settings.get('number_of_tournaments_in_pc'):
        pages = paginate(queryset, page_settings['number_of_tournaments_in_pc'])
    else:
        pages = paginate(queryset, PLAYER_CARD_TOURNAMENTS_PER_PAGE)
    page = get_page(pages, request)
    tournaments = page.get('queryset')
    page_number = page.get('page_number')
    page_range = list(range(1, len(pages) + 1))

    context = {
        'player': player_ex,
        'tournaments': tournaments,
        'number_of_games': number_of_games,
        'number_of_wins': number_of_wins,
        'winning_percentage': winning_percentage,
        'opponents': res,
        'page': page_number,
        'page_range': page_range,
    }
    return render(request, 'pages/player_card.html', context)

