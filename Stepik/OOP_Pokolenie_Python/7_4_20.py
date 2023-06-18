from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=()):
        super().__init__(self._validate(item) for item in iterable)

    @staticmethod
    def _validate(value):
        if isinstance(value, (int, float)):
            return value
        raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def insert(self, index, item):
        self.data.insert(index, self._validate(item))

    def append(self, item):
        self.data.append(self._validate(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self._validate(item) for item in other)

    def __add__(self, other):
        if isinstance(other, (type(self), list)):
            return super().__add__(self._validate(item) for item in other)
        return NotImplemented

    def __iadd__(self, other):
        super().__iadd__(self._validate(item) for item in other)
        return self
