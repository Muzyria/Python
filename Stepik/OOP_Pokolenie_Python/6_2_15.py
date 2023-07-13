import copy

class AttrDict:
    def __init__(self, data=None):
        self.data = data or {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getattr__(self, attr):
        return self.data[attr]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __deepcopy__(self, memo):
        new_data = copy.deepcopy(self.data, memo)
        return AttrDict(new_data)


#test 2
d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)