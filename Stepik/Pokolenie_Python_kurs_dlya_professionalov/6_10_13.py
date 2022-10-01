from collections import ChainMap


def get_all_values(chainmap, key):
    s = set()
    for i in chainmap.maps:
        if key in i:
            s.add(i[key])
    return s



chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
result = get_all_values(chainmap, 'age')
print(*sorted(result))

chainmap = ChainMap({'name': 'Anri', 'city': 'Moscow'}, {'name': 'Arthur', 'city': 'Moscow'},
                    {'name': 'Timur', 'age': 29, 'city': 'Moscow'})
result = get_all_values(chainmap, 'city')
print(*sorted(result))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')
print(*sorted(result))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')
print(result)
