
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        rezult = self.func(*args, **kwargs)
        finish = time.time()
        print(f"Время работы программы {finish - start}")
        return rezult


@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()