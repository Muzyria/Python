

class FieldTracker:
    def __init__(self):
        self._values = {item: getattr(self, item) for item in self.fields}

    def base(self, name) -> int:
        return self._values[name]

    def has_changed(self, name) -> bool:
        return getattr(self, name) != self._values[name]

    def changed(self) -> dict:
        return {k: v for k, v in self._values.items() if self.has_changed(k)}

    def save(self) -> None:
        for k in self.changed().keys():
            self._values[k] = getattr(self, k)



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