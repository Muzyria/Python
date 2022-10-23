def get_all_values(nested_dicts: dict, key):
    keys = set()
    if key in nested_dicts:
        keys.add(nested_dicts[key])
    for k, v in nested_dicts.items():
        if type(v) == dict:
            keys.update(get_all_values(v, key))
    return keys

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')
print(*sorted(result))
# 4 5

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
# math videogames

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')
print(len(sorted(result)))
# 0

# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
# print(*sorted(result))
# print(type(result))
# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_values(my_dict, 'hobby')
# print(*sorted(result))
# 4 5
# <class 'set'>
# math videogames
