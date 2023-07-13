import functools

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if i >= len(self.types):
                    break
                if not isinstance(arg, self.types[i]):
                    raise TypeError("Несоответствие типа аргумента {}".format(i + 1))
            return func(*args, **kwargs)
        return wrapper



@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))
