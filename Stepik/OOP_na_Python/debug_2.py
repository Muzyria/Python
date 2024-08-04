def create_tuples(lst_1: list, lst_2: list) -> list:
    return list(zip(lst_1, lst_2))


print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
