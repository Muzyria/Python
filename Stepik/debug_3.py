

class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def peek(self, default=None):
        if not self.iterable:
            print("TRUE")
        else:
            print("FALSE")

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
iterator.peek()
print(*iterator)

iterator.peek()
print(next(iterator))