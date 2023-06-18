class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        elements = [element % size for element in iterable]
        instance = super().__new__(cls, elements)
        return instance
