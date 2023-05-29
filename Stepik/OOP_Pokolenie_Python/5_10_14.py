class Row:
    def __init__(self, **kwargs):
        [object.__setattr__(self, k, v) for k, v in kwargs.items()]

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, key):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        string = ", ".join([f'{k}={repr(v)}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({string})'

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))


row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)

row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)

row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))
