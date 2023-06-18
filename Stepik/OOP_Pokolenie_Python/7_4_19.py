class AdvancedList(list):
    def join(self, separator=' '):
        return separator.join(str(x) for x in self)

    def map(self, func):
        self[:] = [func(x) for x in self]

    def filter(self, func):
        self[:] = [x for x in self if func(x)]


advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join('-'))
