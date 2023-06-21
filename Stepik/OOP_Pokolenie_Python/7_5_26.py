from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self._items = []
        else:
            self._items = sorted(iterable)

    def __repr__(self):
        return f"SortedList({self._items})"

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._items[index]
        elif isinstance(index, slice):
            return SortedList(self._items[index])
        else:
            raise TypeError("Index must be an integer or slice")

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)
        self._items.sort()

    def discard(self, item):
        self._items = [x for x in self._items if x != item]

    def update(self, iterable):
        self._items.extend(iterable)
        self._items.sort()

    def append(self, item):
        raise NotImplementedError("append() method is not supported")

    def insert(self, index, item):
        raise NotImplementedError("insert() method is not supported")

    def extend(self, iterable):
        raise NotImplementedError("extend() method is not supported")

    def reverse(self):
        raise NotImplementedError("reverse() method is not supported")

    def __reversed__(self):
        raise NotImplementedError("reversed() method is not supported")

    def __setitem__(self, index, value):
        raise NotImplementedError("Setting item value by index is not supported")

    def __delitem__(self, index):
        if isinstance(index, int):
            del self._items[index]
        elif isinstance(index, slice):
            del self._items[index]
        else:
            raise TypeError("Index must be an integer or slice")

    def __mul__(self, n):
        if isinstance(n, int):
            new_items = self._items * n
            return SortedList(new_items)
        else:
            return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __imul__(self, n):
        if isinstance(n, int):
            self._items *= n
            self._items.sort()
            return self
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, SortedList):
            new_items = self._items + other._items
            return SortedList(new_items)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self._items += other._items
            self._items.sort()
            return self
        else:
            return NotImplemented
