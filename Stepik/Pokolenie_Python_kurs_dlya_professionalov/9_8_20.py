import functools


def strip_range(start: int, end: int, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = list(func(*args, **kwargs))


            return ''.join(value)
        return wrapper
    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'
print(beegeek())
