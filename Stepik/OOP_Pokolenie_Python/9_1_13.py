class MultiKeyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aliases = {}

    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        for alias, original_key in self.aliases.items():
            if key == alias:
                return super().__getitem__(original_key)
        raise KeyError(key)

    def alias(self, original_key, alias_key):
        if original_key in self.keys() or alias_key in self.keys() or alias_key in self.aliases.keys():
            raise KeyError("Key or alias already exists")
        self.aliases[alias_key] = original_key

    def __delitem__(self, key):
        if key in self.aliases:
            del self.aliases[key]
        super().__delitem__(key)


multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
print(multikeydict['z'])
multikeydict['t'] += 1
print(multikeydict['x'])

multikeydict.alias('y', 'z')
multikeydict['z'] += [30]
print(multikeydict['y'])
