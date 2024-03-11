

class RandomNumbers:
    def __init__(self, left, right, n):
        self.iterator = iter([__import__("random").randint(left, right) for _ in range(n)])
        self.len_iterator = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.len_iterator:
            self.len_iterator -= 1
            return next(self.iterator)
        raise StopIteration


iterator = RandomNumbers(1, 10, 3)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
print(*iterator)

