from itertools import cycle


class CyclicList:
    def __init__(self, iterable=()):
        self._data = list(iterable) or []

    def append(self, item):
        self._data.append(item)

    def pop(self, index=None):
        if index is None:
            return self._data.pop()
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from cycle(self._data)

    def __getitem__(self, index):
        return self._data[index % len(self._data)]
    

cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')