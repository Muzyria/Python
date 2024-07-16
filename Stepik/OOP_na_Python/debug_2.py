import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        self.func()
        finish = time.time()
        result = finish - start
        print(f"Время работы программы {result}")


@Timer
def calculate():
    for i in range(10000000):
        2**100

calculate()