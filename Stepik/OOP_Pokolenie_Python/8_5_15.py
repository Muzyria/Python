def auto_repr(args, kwargs):
    def decorator(cls):
        class DecoratedClass(cls):
            def __repr__(self):
                attributes = []
                for attr in args:
                    attributes.append(repr(getattr(self, attr)))
                for attr in kwargs:
                    attributes.append(f"{attr}={repr(getattr(self, attr))}")
                return f"{cls.__name__}({', '.join(attributes)})"
        return DecoratedClass
    return decorator



@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)

point.x = 10
point.y = 20
print(point)