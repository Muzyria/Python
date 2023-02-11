class PolyLine:
    def __init__(self, *args):
        self.list_coord = list(args)

    def add_coord(self, x, y):
        self.list_coord.append((x, y))

    def remove_coord(self, indx):
        self.list_coord.pop(indx)

    def get_coords(self):
        return self.list_coord


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))

print(poly.get_coords())
poly.remove_coord(1)
print(poly.get_coords())
