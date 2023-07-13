import functools

def exception_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, Exception):
                return (None, type(result))
            else:
                return (result, None)
        except Exception as e:
            return (None, type(e))
    return wrapper



@exception_decorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2='10'))
