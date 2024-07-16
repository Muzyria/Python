from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        elif isinstance(other, int):
            return self.area == other
        else:
            raise NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        elif isinstance(other, int):
            return self.area > other
        else:
            raise NotImplemented
