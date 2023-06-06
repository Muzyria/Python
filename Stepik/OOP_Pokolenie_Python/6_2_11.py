class SparseArray:
    def __init__(self, default):
        self.lst = []
        self.default = default

    def __getitem__(self, item):
        if item > len(self.lst) - 1:
            return self.default
        return self.lst[item]

    def __setitem__(self, key, value):
        if key >= len(self.lst):
            off = key + 1 - len(self.lst)
            self.lst.extend([self.default] * off)
        self.lst[key] = value


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])
