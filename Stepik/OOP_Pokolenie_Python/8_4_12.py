import functools

class takes_numbers:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Аргументы должны принадлежать типам int или float")
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise TypeError("Аргументы должны принадлежать типам int или float")
        return self.func(*args, **kwargs)


print(takes_numbers)
