class Fibonacci:
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        pass


fibonacci = Fibonacci()
print(next(fibonacci))

fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
