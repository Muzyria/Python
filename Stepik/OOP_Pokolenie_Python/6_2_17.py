class HistoryDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}
        self._history = {key: [value] for key, value in self._data.items()}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self.keys())

    def __delitem__(self, key):
        del self._data[key]
        del self._history[key]

    def __setitem__(self, key, value):
        self._history.setdefault(key, []).append(value)
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]
