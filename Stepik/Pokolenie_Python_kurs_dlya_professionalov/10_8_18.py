# from itertools import zip_longest
#
#
# def roundrobin(*args):
#     for i in zip_longest(*args, fillvalue=''):
#         yield from i

from itertools import cycle

def take(iterable, n):
    for elem, _ in zip(iterable, range(n)):
        yield elem

def roundrobin(*iterables):
    non_empty = len(iterables)
    iterables = cycle(map(iter, iterables))
    while non_empty:
        try:
            for it in iterables:
                yield next(it)
        except StopIteration:
            non_empty -= 1
            iterables = cycle(take(iterables, non_empty))


print(*roundrobin('abc', 'd', 'ef'))
# a d e b f c

numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))
# 1 b 2 e 3 e g e e k

print(list(roundrobin()))
# []
