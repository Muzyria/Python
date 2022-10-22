import functools


def ignore_exception(*arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except arg as err:
                print(f'Исключение {type(err).__name__} обработано')
        return wrapper
    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x
f(0)


min = ignore_exception(ZeroDivisionError)(min)
try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))
