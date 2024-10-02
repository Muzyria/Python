

class Color:
    def __init__(self, hexcode: str):
        self.hexcode = hexcode

    @property
    def hexcode(self) -> str:
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value: str) -> None:
        self._hexcode = value
        self.r, self.g, self.b = int(value[:2], 16), int(value[2:4], 16), int(value[4:], 16)

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)