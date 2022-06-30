class PowerTwo:
    def __init__(self, x):
        self.x = [2**i for i in range(x+1)]

    def __iter__(self):
        return iter(self.x)

    def __next__(self):
        return next(self.x)



numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator)) # печатает 1
print(next(iterator)) # печатает 2
print(next(iterator)) # печатает 4
print(next(iterator)) # исключение StopIteration