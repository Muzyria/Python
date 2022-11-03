from itertools import zip_longest


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)


numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))
# (1, 2) (3, 4) (5, 6)

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))
# (1, 2, 3) (4, 5, 6) (7, None, None)

iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
# (1, 2, 3, None, None)

iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(*grouper(iterator, 4))
# (1, 2, 3, 4) (5, 6, 7, 8) (9, 10, None, None)
