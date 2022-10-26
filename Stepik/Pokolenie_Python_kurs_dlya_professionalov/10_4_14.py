class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.step = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.step += 1
            return self.iterable[self.step]
        except IndexError:
            self.step = 0
            return self.iterable[self.step]



cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

cycle = Cycle([1])
print(next(cycle) + next(cycle) + next(cycle))
