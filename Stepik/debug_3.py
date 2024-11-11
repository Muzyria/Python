class ModularTuple(tuple):
    def __new__(cls, iterable=(), size: int = 100, *args, **kwargs):
        instance = super().__new__(cls, map(lambda x: x % size, iterable))
        return instance

modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)





