class FieldTracker:
    def __init__(self):
        self.changed_values = {}

    def base(self):
        return

    def has_changed(self):
        return

    def changed(self):
        return

    def save(self):
        return


class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())
