from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from ..forms import TableForm
        from tournaments.models import TournamentModel, PlayerModel
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
    players = extract_players(table_body)
    output = {'name': name, 'location': location, 'start_date': start_date, 'finish_date': finish_date,
              'players': players}
    print(output)
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
