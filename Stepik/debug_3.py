

class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    @staticmethod
    def decorator(func):
        def inner(self, *args, **kwargs):
            if isinstance(self, DoubledCounter):
                func(self, *args, **kwargs)
                func(self, *args, **kwargs)
            else:
                func(self, *args, **kwargs)
        return inner

    @decorator
    def inc(self, number: int = 1):
        self.value += number

    @decorator
    def dec(self, number: int = 1):
        self.value -= number
        if self.value < 0:
            self.value = 0

class DoubledCounter(Counter):
    ...



counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)