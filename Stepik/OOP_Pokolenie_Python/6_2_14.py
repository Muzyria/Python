
class OrderedSet:
    def __init__(self, iterable=None):
        self.items = []
        self.index_map = {}
        if iterable is not None:
            for item in iterable:
                self.add(item)

    def add(self, item):
        if item not in self.index_map:
            self.items.append(item)
            self.index_map[item] = len(self.items) - 1

    def discard(self, item):
        if item in self.index_map:
            index = self.index_map.pop(item)
            last_item = self.items.pop()
            if index < len(self.items):
                self.items[index] = last_item
                self.index_map[last_item] = index

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.index_map

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            if len(self) != len(other):
                return False
            return all(a == b for a, b in zip(self, other))
        elif isinstance(other, set):
            return set(self) == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, OrderedSet) or isinstance(other, set):
            return not self == other
        return NotImplemented




