class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())
