
from random import randint

class Elements:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Line(Elements):
    pass    

class Rect(Elements):
    pass

class Ellipse(Elements):
    pass


elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for i in range(217)]
for obj in elements:
    if isinstance(obj, Line):
        obj.ep = (0, 0)
        obj.sp = (0, 0)


