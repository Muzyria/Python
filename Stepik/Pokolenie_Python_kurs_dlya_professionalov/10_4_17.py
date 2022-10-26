class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start != self.end - self.step:
            self.start += self.step
            return self.start
        else:
            raise StopIteration


evens = Xrange(0, 10, 2)
print(*evens)

xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')

xrange = Xrange(10, 1, -1)
print(*xrange)

xrange = Xrange(5, 10)
print(*xrange)

xrange = Xrange(10, -21, -6)
print(list(xrange))
# [10, 4, -2, -8, -14, -20]
