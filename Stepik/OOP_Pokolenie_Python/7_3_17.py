class SuperInt(int):
    def repeat(self, n=2):
        digit = int(str(self) * n)
        return type(self)(digit)

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return type(self)(self + 1)

    def prev(self):
        return type(self)(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))
