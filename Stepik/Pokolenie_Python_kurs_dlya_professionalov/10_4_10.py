class Fibonacci:
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = lambda x: 1 if x in (1, 2) else fib(x - 1) + fib(x - 2)
        return


fibonacci = Fibonacci()
print(next(fibonacci))

fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
