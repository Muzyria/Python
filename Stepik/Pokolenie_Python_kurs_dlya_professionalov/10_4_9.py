class Square:
    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return self.counter ** 2
        raise StopIteration


squares = Square(2)
print(next(squares))
print(next(squares))

squares = Square(10)
print(list(squares))
