# from itertools import pairwise
#
#
# def max_pair(iterable):
#     return max(i + j for i, j in pairwise(iterable))
from itertools import pairwise
max_pair = lambda iterable: max(map(sum, pairwise(iterable)))

print(max_pair([1, 8, 2, 4, 3]))
