class ArithmeticProgression:
    def __init__(self, first, step):
        self.first = first
        self.step = step
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += self.step
        return result


class GeometricProgression:
    def __init__(self, first, ratio):
        self.first = first
        self.ratio = ratio
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current *= self.ratio
        return result



