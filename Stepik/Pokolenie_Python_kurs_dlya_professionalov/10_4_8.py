class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times:
            self.times -= 1
            return self.obj
        else:
            raise StopIteration


bee = BoundedRepeater('bee', 2)
print(next(bee))
print(next(bee))

geek = BoundedRepeater('geek', 3)
print(next(geek))
print(next(geek))
print(next(geek))
try:
    print(next(geek))
except StopIteration:
    print('Error')
