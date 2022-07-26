import json
from garpix_page.models import BasePage
from ..utilities import get_data_from_request


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from ..forms import TableForm
        from tournaments.models import TournamentModel, PlayerModel, GameModel
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = TableForm(request.POST, request.FILES)
            file = request.FILES['table'].readlines()
            print('Received')
            print(request.FILES)
            if form.is_valid():
                form.save()
                t = get_data_from_request(file)
                tournament_results_json = json.dumps({'players': t['players'],
                                                      'results': t['results']}, indent=4)
                TournamentModel.objects.create(name=t['name'], location=t['location'], start_date=t['start_date'],
                                               finish_date=t['finish_date'], results=tournament_results_json)
                new_tournament = TournamentModel.objects.order_by('id').last()
                print(new_tournament)
                for p in t['players']:
                    print(p)
                    if PlayerModel.objects.filter(first_name=p['first_name']).filter(last_name=p['last_name']):
                        print('Exist')
                        PlayerModel.objects.filter(first_name=p['first_name']).filter(last_name=p['last_name'])\
                            .get().tournaments.add(new_tournament)
                    else:
                        print('Create')
                        PlayerModel.objects.create(first_name=p['first_name'],
                                                   last_name=p['last_name']).tournaments.set([new_tournament])
                        print('Created')
                for r in t['results']:
                    player_number = r['player']
                    for i, g in enumerate(r['games']):
                        opponent_number = g['opponent']
                        if opponent_number > player_number:
                            if g['score'] == 0:
                                score = '-'
                            elif g['score'] == 1:
                                score = '+'
                            else:
                                score = '='
                            leg = i + 1
                            player_1 = PlayerModel.objects.filter(first_name=
                                                                  t['players'][player_number - 1]['first_name']).\
                                filter(last_name=t['players'][player_number - 1]['last_name']).get()
                            player_2 = PlayerModel.objects.filter(first_name=
                                                                  t['players'][opponent_number - 1]['first_name']).\
                                filter(last_name=t['players'][opponent_number - 1]['last_name']).get()
                            if 'handicap' in g:
                                GameModel.objects.create(player_1=player_1, player_2=player_2,
                                                         tournament=new_tournament, leg=leg, result=score, handicap=g['handicap'])
                            else:
                                GameModel.objects.create(player_1=player_1, player_2=player_2,
                                                         tournament=new_tournament, leg=leg, result=score)
                            print('Game created')
                print('Valid')
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })
            else:
                print(form.errors.as_data())
            context.update({
                'form': form,
            })
        return context

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ("-created_at",)
