

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(map(lambda x:  f"{x[0]}={repr(x[1])}", self.__dict__.items()))})'

    def __str__(self):
        return f'AnyClass: {", ".join(map(lambda x:  f"{x[0]}={repr(x[1])}", self.__dict__.items()))}'


any = AnyClass()

print(str(any))
print(repr(any))

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))
