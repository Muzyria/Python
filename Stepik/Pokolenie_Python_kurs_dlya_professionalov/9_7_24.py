def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any(map(lambda x: not type(x) is int, [*args, *kwargs.values()])):
            raise TypeError
        elif any(map(lambda x: x <= 0, [*args, *kwargs.values()])):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 55

@takes_positive
def positive_sum(*args):
    return sum(args)
try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))
# <class 'ValueError'>

@takes_positive
def positive_sum(*args):
    return sum(args)
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

@takes_positive
def positive_sum(*args):
    return sum(args)
try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))
# <class 'ValueError'>

@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))
# <class 'ValueError'>

