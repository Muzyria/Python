class PermaDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Изменение значения по ключу невозможно")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if key not in self:
            raise KeyError("Изменение значения по ключу невозможно")
        super().__delitem__(key)

    def keys(self):
        return super().keys()

    def values(self):
        return super().values()

    def items(self):
        return super().items()

    def __len__(self):
        return len(self.keys())
