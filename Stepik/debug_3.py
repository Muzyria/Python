

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.string = ", ".join(list(map(lambda x: f"{x[0]}='{x[1]}'" if isinstance(x[1], str) else f"{x[0]}={x[1]}", self.__dict__.items())))

    def __str__(self):
        return f"{self.__class__.__name__}: {self.string}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.string})"


obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))