class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iterable
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        self.index += self.n
        return self.iterable[self.index - self.n]


skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)