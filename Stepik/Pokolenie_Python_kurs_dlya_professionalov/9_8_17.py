import functools


def prefix(string: str, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return (string + value, value + string)[to_the_end]
        return wrapper
    return decorator


@prefix('€')
def get_bonus():
    return '2000'
print(get_bonus())


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
print(get_bonus())
