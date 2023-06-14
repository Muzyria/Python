import time

class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = self.min = self.max = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args, **kwargs):
        self.last_run = time.perf_counter() - self.start
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)



from time import sleep

timer = AdvancedTimer()

with timer:
    sleep(1.5)
print(round(timer.last_run, 1))

with timer:
    sleep(0.7)
print(round(timer.last_run, 1))

with timer:
    sleep(1)
print(round(timer.last_run, 1))
