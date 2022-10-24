import sys
from functools import lru_cache


@lru_cache()
def func(word):
    return ''.join(sorted(list(word)))


for line in sys.stdin:
    print(func(line.strip('\n')))




