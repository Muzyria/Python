from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in chainmap:
        for i in range(len(chainmap.maps)):
            if key in chainmap.maps[i]:
                chainmap.maps[i][key] = value
    else:
        chainmap[key] = value


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')
print(chainmap)
# Sample Output 1:
# ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)
print(chainmap)
