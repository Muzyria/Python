from random import randint


def random_numbers(left: int, right: int):
    return iter(lambda: randint(left, right), None)


iterator = random_numbers(1, 1)
print(next(iterator))
print(next(iterator))

iterator = random_numbers(1, 10)
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
#
# def power(dergee):
#     def fun(x):
#         return x ** dergee
#     return fun
