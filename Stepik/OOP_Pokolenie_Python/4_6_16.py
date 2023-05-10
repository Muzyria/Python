class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return f'{hex(self.r)[2::].upper():02s}{hex(self.g)[2::].upper():02s}{hex(self.b)[2::].upper():02s}'

    @hexcode.setter
    def hexcode(self, value):
        self.r = int(value[0: 2], 16)
        self.g = int(value[2: 4], 16)
        self.b = int(value[4: 7], 16)


color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
# 0000FF
# 0
# 0
# 255
color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
# A782E3
# 167
# 130
# 227


