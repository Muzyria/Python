def filter_even(func):
    def wrapper(*args, **kwargs):
        args = filter(lambda x: (type(x) is bool and x is False) or
                                (type(x) is int and not x % 2) or
                                (hasattr(x, '__len__') and not len(x) % 2), args)
        return func(*args, **kwargs)
    return wrapper

def delete_short(func):
    def wrapper(*args, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if type(k) is str and len(k) > 4}
        return func(*args, **kwargs)
    return wrapper



@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate([1], [1, 2], {1:1, 2:2}, {1:1}, a="3a", qwer=10, ccccc="Месяцев"))