import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    s = sys.stdout.write
    sys.stdout.write = lambda x: s(x[::-1])
    yield
    sys.stdout.write = s


print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')
