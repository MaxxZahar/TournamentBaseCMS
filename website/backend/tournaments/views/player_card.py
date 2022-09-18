from django.shortcuts import render, get_object_or_404
from ..models import PlayerModel, GameModel


def player(request, player_id):
    player_ex = get_object_or_404(PlayerModel, pk=player_id)
    number_of_games = GameModel.objects.filter(player_1=player_ex).count() \
        + GameModel.objects.filter(player_2=player_ex).count()
    number_of_wins = GameModel.objects.filter(player_1=player_ex).filter(result='+').count() \
        + GameModel.objects.filter(player_2=player_ex).filter(result='-').count()
    winning_percentage = str("%.2f" % round(number_of_wins / number_of_games * 100, 2))
    context = {
        'player': player_ex,
        'number_of_games': number_of_games,
        'number_of_wins': number_of_wins,
        'winning_percentage': winning_percentage
    }
    return render(request, 'pages/player_card.html', context)
