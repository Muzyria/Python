class AnyClass:
    def __init__(self, **kwargs):
        [setattr(self, key, value) for key, value in kwargs.items()]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__dict__}')"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"


any = AnyClass()

print(str(any))
print(repr(any))

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))
# AnyClass: name='John', surname='Marston'
# AnyClass(name='John', surname='Marston')

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))
# AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None
# AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
