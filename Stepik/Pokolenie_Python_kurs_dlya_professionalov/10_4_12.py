class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return key, self.data[key]


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItemsIterator(data)
print(*pairs)