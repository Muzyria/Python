def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any(filter(lambda x: not type(x) is int, args)) or any([type(v) != int for v in kwargs.values()]):
            raise TypeError
        # elif any(filter(lambda x: x < 1, args)): я хз почему это не срабатывает
        elif any([i <= 0 for i in args]) or any([v <= 0 for v in kwargs.values()]):
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

