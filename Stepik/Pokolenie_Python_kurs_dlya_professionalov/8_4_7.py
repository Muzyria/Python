def get_all_values(nested_dicts, key, d=list()):
    if key in nested_dicts:
        # return nested_dicts[key]
        d.append(nested_dicts[key])

    for k, v in nested_dicts.items():
        if type(v) == dict:
            value = get_all_values(v, key)
            # if value is not None:
            #     # print(value)
            #     # return value
            #     d.append(value)
    return d


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')
print(*sorted(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')
print(*sorted(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')
print(len(sorted(result)))

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
