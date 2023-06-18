class MutableString:
    def __init__(self, initial_string):
        self.data = initial_string

    def __repr__(self):
        return self.data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        chars = list(self.data)
        chars[index] = value
        self.data = "".join(chars)

    def __delitem__(self, index):
        chars = list(self.data)
        del chars[index]
        self.data = "".join(chars)

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))
