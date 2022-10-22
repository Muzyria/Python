import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if type(value) == datatype:
                return value
            else:
                raise TypeError()
        return wrapper
    return decorator


@returns(int)
def add(a, b):
    return a + b
print(add(10, 5))

@returns(int)
def add(a, b):
    return a + b

try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))

