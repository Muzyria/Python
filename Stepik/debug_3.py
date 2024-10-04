
class Rectangle:
    def __init__(self, length: int, width: int):
        self. length = length
        self.width = width

    @classmethod
    def square(cls, side: int) -> "Rectangle":
        return cls(side, side)

