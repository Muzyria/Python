def dates(start, count=None):
    pass


generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))

generator = dates(date(2022, 3, 8), 5)
print(*generator)
