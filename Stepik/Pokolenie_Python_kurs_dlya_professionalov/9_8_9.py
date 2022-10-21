import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper


@square
def add(a, b):
    return a + b
print(add(3, 7))


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b
print(add(1, 1))
print(add.__name__)
print(add.__doc__)
