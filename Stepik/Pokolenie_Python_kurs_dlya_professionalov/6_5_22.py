from collections import defaultdict


def wins(pairs):
    name_players = defaultdict(set)
    for key, value in pairs:
        name_players[key].add(value)
    return name_players

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))
