from django.shortcuts import render, get_object_or_404
from ..models import TournamentModel


def tournament(request, tournament_id):
    context = {
        'tournament': get_object_or_404(TournamentModel, pk=tournament_id)
    }
    return render(request, 'pages/tournament_card.html', context)
