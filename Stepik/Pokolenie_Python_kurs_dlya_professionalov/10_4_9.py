class Square:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i != self.n:
            self.i += 1
            return self.i ** 2
        else:
            raise StopIteration


squares = Square(2)
print(next(squares))
print(next(squares))

squares = Square(10)
print(list(squares))
