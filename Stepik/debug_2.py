

class AttrDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self._data = data.copy()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getattr__(self, attr):
        return self._data[attr]

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value



# attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})
#
#
# print(attrdict['name'])
# print(attrdict.father)
# print(len(attrdict))
#
# attrdict = AttrDict()
#
# attrdict['school_name'] = 'BEEGEEK'
# print(attrdict['school_name'])
# print(attrdict.school_name)

d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)