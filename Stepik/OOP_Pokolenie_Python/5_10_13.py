class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {repr(self.color)})'

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return (self.x, self.y, self.color) == (other.x, other.y, other.color)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


points = [ColoredPoint(10, 100, 'OliveDrab'), ColoredPoint(73, 76, 'SpringGreen'), ColoredPoint(67, 98, 'Black'),
          ColoredPoint(98, 86, 'DarkGray'), ColoredPoint(28, 29, 'LightYellow'), ColoredPoint(38, 73, 'Coral'),
          ColoredPoint(79, 41, 'DarkGray'), ColoredPoint(51, 83, 'DarkGreen'), ColoredPoint(40, 95, 'BlanchedAlmond'),
          ColoredPoint(84, 65, 'Azure'), ColoredPoint(30, 9, 'DarkSlateBlue'), ColoredPoint(5, 59, 'SkyBlue'),
          ColoredPoint(98, 24, 'Chartreuse'), ColoredPoint(60, 8, 'LightCyan'), ColoredPoint(94, 31, 'YellowGreen'),
          ColoredPoint(36, 30, 'DarkOliveGreen'), ColoredPoint(49, 30, 'Beige'), ColoredPoint(36, 28, 'Chocolate'),
          ColoredPoint(19, 95, 'AntiqueWhite'), ColoredPoint(13, 13, 'AntiqueWhite'),
          ColoredPoint(78, 46, 'LightCoral'), ColoredPoint(56, 25, 'LightSkyBlue'), ColoredPoint(34, 12, 'Magenta'),
          ColoredPoint(49, 22, 'SlateGray'), ColoredPoint(89, 8, 'DarkGoldenRod'), ColoredPoint(39, 84, 'Salmon'),
          ColoredPoint(73, 96, 'MintCream'), ColoredPoint(10, 65, 'MintCream'), ColoredPoint(67, 48, 'Peru'),
          ColoredPoint(76, 13, 'Orchid'), ColoredPoint(11, 73, 'Olive'), ColoredPoint(12, 88, 'Silver'),
          ColoredPoint(89, 85, 'PaleVioletRed'), ColoredPoint(68, 6, 'Purple'), ColoredPoint(56, 64, 'Red'),
          ColoredPoint(7, 25, 'LightGray'), ColoredPoint(41, 76, 'Salmon'), ColoredPoint(28, 99, 'CornflowerBlue'),
          ColoredPoint(47, 7, 'LightSeaGreen'), ColoredPoint(85, 100, 'PeachPuff'), ColoredPoint(5, 86, 'Cyan'),
          ColoredPoint(68, 11, 'Violet'), ColoredPoint(49, 31, 'Violet'), ColoredPoint(93, 55, 'LightCyan'),
          ColoredPoint(8, 42, 'PeachPuff'), ColoredPoint(46, 43, 'Teal'), ColoredPoint(67, 36, 'Navy'),
          ColoredPoint(64, 50, 'Olive'), ColoredPoint(8, 59, 'PaleTurquoise'), ColoredPoint(79, 69, 'Salmon'),
          ColoredPoint(81, 37, 'Fuchsia'), ColoredPoint(86, 84, 'Orchid'), ColoredPoint(25, 100, 'DeepSkyBlue'),
          ColoredPoint(12, 15, 'IndianRed'), ColoredPoint(9, 71, 'LimeGreen'), ColoredPoint(88, 23, 'WhiteSmoke'),
          ColoredPoint(12, 89, 'DodgerBlue'), ColoredPoint(12, 19, 'BurlyWood'), ColoredPoint(12, 66, 'MediumOrchid'),
          ColoredPoint(59, 55, 'PaleGreen'), ColoredPoint(15, 86, 'Black'), ColoredPoint(65, 98, 'DarkOliveGreen'),
          ColoredPoint(86, 83, 'DarkGoldenRod'), ColoredPoint(9, 85, 'DarkOliveGreen'),
          ColoredPoint(73, 46, 'WhiteSmoke'), ColoredPoint(77, 88, 'Beige'), ColoredPoint(43, 64, 'MediumBlue'),
          ColoredPoint(95, 84, 'DodgerBlue'), ColoredPoint(11, 63, 'DarkGray'), ColoredPoint(28, 71, 'DarkSalmon'),
          ColoredPoint(11, 81, 'AliceBlue'), ColoredPoint(80, 26, 'LightCoral'), ColoredPoint(97, 35, 'Tomato'),
          ColoredPoint(12, 82, 'Sienna'), ColoredPoint(100, 23, 'Moccasin'), ColoredPoint(45, 95, 'SeaGreen'),
          ColoredPoint(94, 70, 'LightYellow'), ColoredPoint(63, 76, 'Beige'), ColoredPoint(29, 16, 'FireBrick'),
          ColoredPoint(21, 42, 'HotPink'), ColoredPoint(65, 63, 'DarkOrange'), ColoredPoint(31, 14, 'HotPink'),
          ColoredPoint(55, 67, 'DarkSeaGreen'), ColoredPoint(98, 86, 'YellowGreen'),
          ColoredPoint(60, 36, 'LightSteelBlue'), ColoredPoint(11, 32, 'RoyalBlue'), ColoredPoint(14, 93, 'Red'),
          ColoredPoint(72, 74, 'Fuchsia'), ColoredPoint(53, 98, 'AntiqueWhite'), ColoredPoint(20, 33, 'Gold'),
          ColoredPoint(64, 24, 'LightCyan'), ColoredPoint(96, 58, 'PapayaWhip'), ColoredPoint(57, 79, 'SlateGray'),
          ColoredPoint(47, 75, 'MediumSpringGreen'), ColoredPoint(79, 73, 'Silver'), ColoredPoint(60, 36, 'DodgerBlue'),
          ColoredPoint(86, 12, 'Linen'), ColoredPoint(9, 7, 'RoyalBlue'), ColoredPoint(77, 70, 'Navy'),
          ColoredPoint(83, 66, 'LightCyan')]

for point in points:
    print(point.x, point.y, point.color)


