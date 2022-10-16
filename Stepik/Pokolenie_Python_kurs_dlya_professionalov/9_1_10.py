def is_greater(lists: list, number: int):
    return any(sum(i) > number for i in lists)


data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))
