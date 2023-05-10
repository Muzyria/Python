class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(length=side, width=side)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)

rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)
