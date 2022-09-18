def frequency_dict(q, player_id):
    freq = {}
    for game in q:
        if game['player_1'] == player_id:
            if freq.get(game['player_2']):
                freq[game['player_2']][0] += 1
                if game['result'] == '+':
                    freq[game['player_2']][1] += 1
            else:
                if game['result'] == '+':
                    freq[game['player_2']] = [1, 1]
                else:
                    freq[game['player_2']] = [1, 0]
        else:
            if freq.get(game['player_1']):
                freq[game['player_1']][0] += 1
                if game['result'] == '-':
                    freq[game['player_1']][1] += 1
            else:
                if game['result'] == '-':
                    freq[game['player_1']] = [1, 1]
                else:
                    freq[game['player_1']] = [1, 0]
    return freq


def gain_max_element_of_freq_dict(freq):
    max_value = 0
    max_key = 0
    wins = 0
    for el in freq.items():
        if el[1][0] > max_value:
            max_value = el[1][0]
            max_key = el[0]
            wins = el[1][1]
    return [max_key, max_value, wins]


def gain_opponents_list(freq, n):
    from ..models import PlayerModel
    opponents = []
    opponents_item = {}
    while n:
        if freq:
            max_opponent = gain_max_element_of_freq_dict(freq)
            opponents_item['opponent'] = PlayerModel.objects.filter(id=max_opponent[0]).get()
            opponents_item['games'] = max_opponent[1]
            opponents_item['wins'] = max_opponent[2]
            opponents.append(opponents_item)
        else:
            return opponents
        n -= 1
        freq.pop(max_opponent[0])
        opponents_item = {}
    return opponents
