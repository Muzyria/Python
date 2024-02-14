from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



