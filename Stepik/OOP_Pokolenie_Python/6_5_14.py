import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.original = data
        self.copy = copy.deepcopy if deep else copy.copy

        if isinstance(data, list):
            self.original_update = self.original.extend
        elif isinstance(data, (set, dict)):
            self.original_update = self.original.update

    def __enter__(self):
        self.data = self.copy(self.original)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original_update(self.data)
        return True
