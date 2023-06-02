class SparseArray:
    def __init__(self, default):
        self.lst = []
        self.default = default

    def __getitem__(self, item):
        return

    def __setitem__(self, key, value):
        if key >= len(self.lst):
            off = key + 1 - len(self.lst)
            self.lst.extend([self.default] * off)
        self.lst[key] = value
