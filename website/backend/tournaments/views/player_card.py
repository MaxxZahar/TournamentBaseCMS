from django.shortcuts import render, get_object_or_404
from ..models import PlayerModel


def player(request, player_id):
    context = {
        'player': get_object_or_404(PlayerModel, pk=player_id)
    }
    return render(request, 'pages/player_card.html', context)
