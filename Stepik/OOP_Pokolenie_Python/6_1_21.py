class LoopTracker:
    NO_VALUE = object()

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._accesses = self._empty_accesses = 0
        self._cached = self._first = self._last = self.NO_VALUE

    def __iter__(self):
        return self

    def __next__(self):
        item = self._get_next()
        if item is self.NO_VALUE:
            self._empty_accesses += 1
            return next(self._iterator)
        self._last = item
        self._accesses += 1
        return item

    def _get_next(self):
        if self._first is self.NO_VALUE:
            item = self._first = next(self._iterator, self.NO_VALUE)
        elif self._cached is not self.NO_VALUE:
            item = self._cached
            self._cached = self.NO_VALUE
        else:
            item = next(self._iterator, self.NO_VALUE)
        return item

    def is_empty(self):
        if self._cached is self.NO_VALUE:
            self._cached = self._get_next()
        return self._cached is self.NO_VALUE

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is self.NO_VALUE:
            if self.is_empty():
                raise AttributeError('Исходный итерируемый объект пуст')
        return self._first

    @property
    def last(self):
        if self._last is self.NO_VALUE:
            raise AttributeError('Последнего элемента нет')
        return self._last
