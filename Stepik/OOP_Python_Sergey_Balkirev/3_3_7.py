class Complex:
    def __init__(self, real, img):
        self.__real = None
        self.__img = None
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")


    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

