
class Rectangle:
    def __init__(self, h, w):
        self.__area = h * w

    @property
    def area(self):
        return self.__area


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6        