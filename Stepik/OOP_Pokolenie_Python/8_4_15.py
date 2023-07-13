import functools

def ignore_exception(*exception_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                print("Исключение {} обработано".format(type(e).__name__))
        return wrapper
    return decorator



@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    """beegeek"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())
