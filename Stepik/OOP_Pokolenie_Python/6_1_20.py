SENTINEL = object()


class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        self.peek()
        return self.cache.pop()

    def peek(self, default=SENTINEL):
        if not self.cache:
            try:
                self.cache.append(next(self.iterator))
            except StopIteration:
                if default is not SENTINEL:
                    return default
                raise
        return self.cache[0]


iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)
