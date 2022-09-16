from django.shortcuts import render, get_object_or_404
from ..models import TournamentModel, PlayerModel


def tournament(request, tournament_id):
    tournament_record = get_object_or_404(TournamentModel, pk=tournament_id)
    tournament_table_row = {}
    table = []
    players = tournament_record.get_players()
    results = tournament_record.get_results()
    for i, player in enumerate(players):
        tournament_table_row['place'] = i + 1
        tournament_table_row['first_name'] = player['first_name']
        tournament_table_row['last_name'] = player['last_name']
        score = 0
        res = ''
        for game in results[i]['games']:
            score += game['score']
            res += str(game['opponent'])
            if game['score'] == 1:
                res += '+'
            elif game['score'] == 0:
                res += '-'
            else:
                res += '='
            if len(players) < 10:
                res += ' '
            elif len(players) < 100:
                if game['opponent'] > 9:
                    res += ' '
                else:
                    res += ' ' * 2
            else:
                if game['opponent'] > 99:
                    res += ' '
                elif game['opponent'] > 9:
                    res += ' ' * 2
                else:
                    res += ' ' * 3
        tournament_table_row['results_string'] = res
        tournament_table_row['score'] = score
        tournament_table_row['id'] = \
            PlayerModel.objects.filter(first_name=player['first_name']).filter(last_name=player['last_name'])\
            .values_list('id', flat=True).first()
        table.append(tournament_table_row)
        tournament_table_row = {}
    context = {
        'tournament': get_object_or_404(TournamentModel, pk=tournament_id),
        'table': table
    }
    return render(request, 'pages/tournament_card.html', context)
