class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return None

    def keys_of(self, value):
        return [k for k, v in self.items() if v == value]


valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))
