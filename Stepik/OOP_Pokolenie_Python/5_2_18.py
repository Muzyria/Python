class AnyClass:
    def __init__(self, **kwargs):
        [setattr(self, key, value) for key, value in kwargs.items()]

    def __repr__(self):
        attrs = ', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

    def __str__(self):
        attrs = ", ".join(f'{k}={repr(v)}' for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}: {attrs}"


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
