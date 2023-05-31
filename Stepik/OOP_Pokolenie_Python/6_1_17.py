class AttrsIterator:
    def __init__(self, obj):
        self._obj = list(obj.__dict__.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self._obj):
            raise StopIteration
        return self._obj[self.index]



class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)
