from itertools import count


def tabulate(func):
    count1 = count()


func = lambda x: x
values = tabulate(func)
print(next(values))
print(next(values))
