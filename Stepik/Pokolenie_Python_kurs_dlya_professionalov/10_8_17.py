from itertools import cycle
from string import ascii_uppercase


def alnum_sequence():
    for val in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from (i for i in val)


alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(100)))
