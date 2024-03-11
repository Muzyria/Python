
class Xrange:
    def __init__(self, start, end, step=1):
        self.step = step
        self.end = end
        self.start = start - step


    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start >= self.end and self.step > 0:
            raise StopIteration
        if self.start <= self.end and self.step < 0:
            raise StopIteration
        return self.start



xrange = Xrange(5, 10)

print(*xrange)