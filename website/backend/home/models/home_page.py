from django.db import models
from garpix_page.models import BasePage


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
                TournamentModel.objects.create(name=t['name'], location=t['location'], start_date=t['start_date'],
                                               finish_date=t['finish_date'])
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


def get_data_from_request(file):
    table = []
    for line in file:
        if line.strip():
            table.append(line.decode('UTF-8'))
    table_header = table[0].strip()
    table_body = table[1:]
    print(len(table_body))
    output = extract_tournament_info(table_header)
    players = extract_players(table_body)
    results = get_all_results(table_body)
    output.update({'players': players})
    output.update({'results': results})
    print(output)
    return output


def extract_tournament_info(table_header):
    left_comma_index = table_header.index(',')
    right_comma_index = table_header.rindex(',')
    name = table_header[1:left_comma_index].strip()
    location = table_header[left_comma_index + 1:right_comma_index].strip()
    date = table_header[right_comma_index + 1:-1].strip()
    if len(date) == 10:
        start_date = date
        finish_date = date
    elif len(date) == 23:
        start_date = date[:10]
        finish_date = date[13:]
    elif len(date) == 21:
        start_date = date[:10]
        finish_date = date[11:]
    else:
        raise ValueError('Wrong date format')
    output = {'name': name, 'location': location, 'start_date': start_date, 'finish_date': finish_date}
    return output


def extract_players(table):
    import re
    players = []
    for line in table:
        print(line)
        player = {}
        player['last_name'] = re.search(r'\[.*?\]', line).group(0)[1:-1].strip()
        rb_index = line.index(']')
        player['first_name'] = re.search(
            r'\[.*?\]', line[rb_index + 1:]).group(0)[1:-1].strip()
        print(player)
        players.append(player)
    return players


def get_results_string(line):
    import re
    lb_index = line.rindex('[')
    string = re.search(r'\[.*\]', line[lb_index:]
                       ).group(0).strip()[1:-1].strip()
    string = string.replace(" ", "").replace('\t', '')
    return string


def get_results(line):
    string = get_results_string(line)
    # print(string)
    # print(len(string))
    separators = {'+', '-', '='}
    current = ''
    results = []
    is_handicap = False
    handicap = ''
    result = {}

    for i, s in enumerate(string):
        # print(s)
        if s not in separators and not is_handicap and not s == '(':
            current += s
        elif s in separators and not is_handicap:
            result['opponent'] = int(current)
            if s == '+':
                result['score'] = 1
            elif s == '-':
                result['score'] = 0
            else:
                result['score'] = 0.5
            current = ''
            if (i < len(string) - 1 and not string[i + 1] == '(') or i == len(string) - 1:
                results.append(result)
                result = {}
        elif s == '(':
            is_handicap = True
        elif s == ')':
            is_handicap = False
            result['handicap'] = handicap
            handicap = ''
            results.append(result)
            result = {}
        elif is_handicap:
            handicap += s
    return results


def get_all_results(table):
    results = []
    for i, line in enumerate(table):
        result = {}
        result['player'] = i + 1
        result['games'] = get_results(line)
        results.append(result)
    return results
