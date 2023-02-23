class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)


p1 = MyPoint(3, 4)
p2 = MyPoint(5, 12)
p3 = p1 + p2
print(p3.__dict__)
print(p3.x + p3.y)