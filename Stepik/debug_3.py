

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return sum(self.__dict__.values())

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())