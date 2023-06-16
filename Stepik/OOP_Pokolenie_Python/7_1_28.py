class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, x=1):
        self.value += x

    def dec(self, x=1):
        self.value -= x
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, x=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, x=1):
        self.value += x
        if self.value > self.limit:
            self.value = self.limit


counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
