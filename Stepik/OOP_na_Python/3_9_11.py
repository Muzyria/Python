# Напишите определение класса Countdown
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


# Ниже код для проверки методов класса Countdown

count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)
