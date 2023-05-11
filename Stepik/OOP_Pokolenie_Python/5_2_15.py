class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


vector = Vector(1, 2)

print(str(vector))
print(repr(vector))
