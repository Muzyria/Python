class TreeBuilder:
    def __init__(self):
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()

    def add(self, value):
        self.knots[-1].append(value)

    def structure(self):
        return self.knots[-1]
