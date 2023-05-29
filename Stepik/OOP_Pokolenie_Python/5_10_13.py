class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return (self.x, self.y, self.color) == (other.x, other.y, other.color)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))

points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)

point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')


