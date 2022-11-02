from itertools import islice

# def take(iterable, n):
#     yield from islice(iterable, n)

take = lambda i, n: islice(i, n)

print(*take(range(10), 5))


iterator = iter('beegeek')
print(*take(iterator, 22))

iterator = iter('beegeek')
print(*take(iterator, 1))
