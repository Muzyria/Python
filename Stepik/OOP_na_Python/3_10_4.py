class InfinityIterator:
        def __init__(self):
            self.num = 0

        def __iter__(self):
            return self

        def __next__(self):
            num = self.num
            self.num += 10
            return num 



a = iter(InfinityIterator())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
