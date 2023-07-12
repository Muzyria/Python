from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y != 0:
            self.quadrant = (1, 4)[self.y < 0]
        elif self.x < 0 and self.y != 0:
            self.quadrant = (2, 3)[self.y < 0]

    def symmetric_x(self):
        return type(self)(self.x, -self.y)

    def symmetric_y(self):
        return type(self)(-self.x, self.y)


point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)
