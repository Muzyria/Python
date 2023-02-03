class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    def __init__(self, x=0, y=0):
        self.__x = x if self.check_val(x) else 0
        self.__y = y if self.check_val(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.check_val(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.check_val(y):
            self.__y = y

    @classmethod
    def check_val(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
