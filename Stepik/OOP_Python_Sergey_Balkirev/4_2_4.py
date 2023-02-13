class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            if self.__check_item(i):
                self.append(i)
        super().__init__(lst)        

    @staticmethod
    def __check_item(x):
        if type(x) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return True

    def __setitem__(self, key, value):
        self.__check_item(value)
        super().__setitem__(key, value)

    def append(self, value):
        if self.__check_item(value):
            super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
