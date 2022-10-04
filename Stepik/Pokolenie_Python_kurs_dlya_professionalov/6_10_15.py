from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if from_left == True and key in chainmap:
        return chainmap[key]
    if from_left == False and key in chainmap:
        return chainmap.maps[::-1][0][key]

# from collections import ChainMap
#
# def get_value(chainmap, key, from_left=True):
#     if not from_left:
#         chainmap.maps.reverse()
#     return chainmap.get(key)



chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'name', False))
