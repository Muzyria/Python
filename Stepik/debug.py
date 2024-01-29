

class Gun:
    def shoot(self):
        print('pif')


gun = Gun()

gun.shoot()


class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self) -> str:
        return self._hexcode

    @property
    def r(self) -> int:
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @hexcode.setter
    def hexcode(self, value: str) -> None:
        self._hexcode = value
        self._r = int(value[0: 2], 16)
        self._g = int(value[2: 4], 16)
        self._b = int(value[4: 7], 16)


color = Color('0000FF')
print(color.__dict__)

color.hexcode = 'A782E3'
print(color.__dict__)
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)