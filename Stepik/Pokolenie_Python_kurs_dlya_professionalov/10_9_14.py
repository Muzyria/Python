from itertools import dropwhile


# def first_true(iterable, predicate):
#     if predicate is None:
#         predicate = bool
#     return next(dropwhile(lambda elem: not predicate(elem), iterable), None)


def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)


numbers = [1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))
# 2

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))
# 100

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
print(first_true(numbers, None))
# 69
