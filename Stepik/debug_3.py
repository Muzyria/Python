

class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool = False):
        self.start = start
        self.end = end
        self.cache = cache
        if self.cache:
            self.first_value = __import__("random").randint(self.start, self.end)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if hasattr(self, "first_value"):
            return self.first_value
        return __import__("random").randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")

class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
