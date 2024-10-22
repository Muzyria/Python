
class SparseArray:
    def __init__(self, default):
        self.default = default
        self.data = []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        if key >= len(self.data):
            return self.default
        return self.data[key]

    def __setitem__(self, key, value):
        if key > (len(self.data) - 1):
            self.data.extend([self.default] * (key - len(self.data) + 1))
        self.data[key] = value


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])
