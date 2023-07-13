import math

class Vector:
    def __init__(self, *args):
        self.coordinates = args

    def __str__(self):
        return "(" + ", ".join(str(coord) for coord in self.coordinates) + ")"

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь равную длину")
        new_coordinates = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)

    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь равную длину")
        new_coordinates = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(*new_coordinates)

    def __mul__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь равную длину")
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.coordinates))

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all(x == y for x, y in zip(self.coordinates, other.coordinates))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.coordinates)




vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)