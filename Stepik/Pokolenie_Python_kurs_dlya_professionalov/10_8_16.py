# from itertools import accumulate
# from math import factorial
#
#
# def factorials(n):
#     for i in range(1, n + 1):
#         yield factorial(i)
from itertools import accumulate
import operator


def factorials(n):
    return accumulate(range(1, n + 1), operator.mul)


numbers = factorials(6)
print(*numbers)

numbers = factorials(2)
print(next(numbers))
print(next(numbers))
