from itertools import pairwise


# def is_rising(iterable):
#     for i in pairwise(iterable):
#         if i[0] < i[1]:
#             continue
#         else:
#             return False
#     return True

from itertools import pairwise

def is_rising(iterable):
    return all(a < b for a, b in pairwise(iterable))


print(is_rising([1, 2, 3, 4, 5]))
