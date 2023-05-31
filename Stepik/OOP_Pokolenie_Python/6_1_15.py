class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        return (elem for elem in self.__dict__.values())


point = Point(1, 2, 3)

print(list(point))
