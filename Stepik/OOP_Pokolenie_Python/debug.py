def takes_positive(func):
    def wrapper(*args, **kwargs):
        if not all(type(i) == int for i in [*args, *kwargs.values()]):
            raise TypeError
        elif not all(i > 0 for i in [*args, *kwargs.values()]):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))