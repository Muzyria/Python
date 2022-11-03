from itertools import tee


def ncycles(iterable, times):
    for i in tee(iterable, times):
        yield from i


print(*ncycles([1, 2, 3, 4], 3))

iterator = iter('bee')
print(*ncycles(iterator, 4))

iterator = iter([1])
print(*ncycles(iterator, 10))
