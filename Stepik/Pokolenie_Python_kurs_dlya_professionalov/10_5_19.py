from datetime import date


def dates(start, count=None):
    start = date.toordinal(start)
    if count is None:
        while True:
            yield date.fromordinal(start)
            start += 1
    else:
        for i in range(start, start + count):
            yield date.fromordinal(i)


generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))

generator = dates(date(2022, 3, 8), 5)
print(*generator)
