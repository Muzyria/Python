class Grouper:
    def __init__(self, iterable, key):
        self._iterable = list(iterable)
        self._key = key
        self._make_groups(self._iterable)

    def _make_groups(self, iterable):
        self._groups = {}
        for item in iterable:
            self.add(item)

    def add(self, item):
        self._groups.setdefault(self._key(item), []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._groups)

    def __iter__(self):
        return iter(self._groups.items())

    def __contains__(self, item):
        return item in self._groups

    def __getitem__(self, key):
        return self._groups[key]
