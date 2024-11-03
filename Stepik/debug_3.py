

class FieldTracker:
    atr = {}

    def __init__(self):
        self.atr.update(self.__dict__)

    def base(self, name: str):
        return self.atr[name]

    def has_changed(self, name: str) -> bool:
        return self.__dict__[name] != self.atr[name]

    def changed(self) -> dict:
        return {x: self.atr[x] for x in self.__dict__ if self.has_changed(x)}

    def save(self) -> None:
        for name, value in self.__dict__.items():
            if self.has_changed(name):
                self.atr[name] = value


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())