from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.elements = []
        for arg in args:
            if isinstance(arg, int):
                self.elements.append(arg)
            elif isinstance(arg, str):
                start, end = map(int, arg.split('-'))
                self.elements.extend(range(start, end + 1))

    def __getitem__(self, index):
        return self.elements[index]

    def __len__(self):
        return len(self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __reversed__(self):
        return reversed(self.elements)
