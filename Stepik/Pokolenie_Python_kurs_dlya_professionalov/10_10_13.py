from itertools import chain


def sum_of_digits(iterable):
    return sum(int(j) for i in chain(iterable) for j in str(i))


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
