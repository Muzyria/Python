from copy import deepcopy

list_of_dicts = [
    {"id": 1, "value": [10, 20]},
    {"id": 2, "value": [30, 40]}
]

copy_data = deepcopy(list_of_dicts)



list_of_dicts[0]["value"][0] = 999


print(list_of_dicts)
print(copy_data)



