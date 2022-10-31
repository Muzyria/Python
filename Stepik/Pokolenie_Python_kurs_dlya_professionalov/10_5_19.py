from datetime import date


def dates(start, count=None):
    start = date.toordinal(start)
    if count is None:
        while True:
            if start <= 3652059:
                yield date.fromordinal(start)
                start += 1
            else:
                return None
    else:
        for i in range(start, start + count):
            yield date.fromordinal(i)


generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))

generator = dates(date(2022, 3, 8), 5)
print(*generator)

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
try:
    print(next(generator))
except StopIteration:
    print('Error')
# 9999-12-21
# 9999-12-22
# 9999-12-23
# 9999-12-24
# 9999-12-25
# 9999-12-26
# 9999-12-27
# 9999-12-28
# 9999-12-29
# 9999-12-30
# 9999-12-31
# Error

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
try:
    print(next(generator))
except StopIteration:
    print('Error')
# 9999-12-21
# 9999-12-22
# 9999-12-23
# 9999-12-24
# 9999-12-25
# 9999-12-26
# 9999-12-27
# 9999-12-28
# 9999-12-29
# 9999-12-30
# 9999-12-31
# Error

