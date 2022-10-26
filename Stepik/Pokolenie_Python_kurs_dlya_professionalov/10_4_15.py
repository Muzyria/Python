from random import randint


class RandomNumbers:
    def __init__(self, left, right, n):
        self.n = n
        self.left = left
        self.right = right

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return randint(self.left, self.right)


iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
