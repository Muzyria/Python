class SkipIterator:
    def __init__(self, iterable, n):
        lst = list(iterable)
        self.iterable = (lst[i] for i in range(0, len(lst), n + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)