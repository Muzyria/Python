from itertools import count


def tabulate(func):
    yield from (func(i) for i in count(1))


func = lambda x: x
values = tabulate(func)
print(next(values))
print(next(values))

func = lambda x: x + 10
values = tabulate(func)
print(next(values))
print(next(values))
print(next(values))
