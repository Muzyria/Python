import functools

class MaxCallsException(Exception):
    pass

def limited_calls(n):
    def decorator(func):
        count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            if count > n:
                raise MaxCallsException("Превышено допустимое количество вызовов")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limited_calls(10)
def power(a, n):
    """degree"""
    return a ** n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))

