class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = None
        self.__height = None
        self.width = width
        self.height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @classmethod
    def check_val(cls, value):
        return type(value) == int and value in range(10001)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.check_val(value):
            if self.__width:
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.check_val(value):
            if self.__height:
                self.show()
            self.__height = value


w = WindowDlg("qwerty", -10, 20)
w.show()
w.width = 50
w.height = 50

q = WindowDlg("qwerty", -10, 20)
q.show()
