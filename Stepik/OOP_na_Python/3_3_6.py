class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f'Rectangle({self.width}x{self.height})'


# Напишите определение класса Rectangle


# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
print(r3)
