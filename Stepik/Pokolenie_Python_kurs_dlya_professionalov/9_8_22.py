import functools


def takes(*arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all(map(lambda x: type(x) in arg, [*args, *kwargs.values()])):
                return func(*args, **kwargs)
            raise TypeError()
        return wrapper
    return decorator




@takes(int, str)
def repeat_string(string, times):
    return string * times
print(repeat_string('bee', 3))

@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b
print(add.__name__)
print(add.__doc__)
try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))
