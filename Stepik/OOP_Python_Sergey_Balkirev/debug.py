class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [ i for i in range(1, 2001, 2)]
print(len(points))
