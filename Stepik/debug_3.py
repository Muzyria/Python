
class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = iter(map(lambda x: (x, data[x]), data))

    def __iter__(self):
        return self

    def __next__(self):
        if self.data:
            return next(self.data)
        raise StopIteration


data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
        'Anri': [100, 101], 'Roma': [99]}

pairs = DictItemsIterator(data)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')