class RandomLooper:
    def __init__(self, *args):
        self.looper = []
        [self.looper.extend(item) for item in args]
        __import__('random').shuffle(self.looper)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.looper):
            raise StopIteration
        return self.looper[self.index]


colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))
