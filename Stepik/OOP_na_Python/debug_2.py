from typing import Generator

def my_range_gen(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    if step == 0:
        return
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


for i in my_range_gen(5):
    print(i)

for i in my_range_gen(10, 20):
    print(i)

for i in my_range_gen(10, 30, 3):
    print(i)
