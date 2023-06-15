import random

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.generated_number = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache and self.generated_number is not None:
            return self.generated_number
        number = random.randint(self.start, self.end)
        if self.cache:
            self.generated_number = number
        return number

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")
