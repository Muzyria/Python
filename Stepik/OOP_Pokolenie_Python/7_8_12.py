from collections import OrderedDict


class Queue:
    def __init__(self, initial_data=None):
        self.data = OrderedDict()
        if initial_data is not None:
            self.data.update(initial_data)

    def add(self, item):
        key, value = item
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value

    def pop(self):
        try:
            return self.data.popitem(last=False)
        except KeyError as e:
            e.args = ('Очередь пуста',)
            raise

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f'Queue({list(self.data.items())})'
