from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


val = groupby(sorted(persons, key=lambda x: x.height), key=lambda x: x.height)
for k, v in val:
    print(f'{k}: {", ".join(sorted(str(x.name) for x in v))}')
