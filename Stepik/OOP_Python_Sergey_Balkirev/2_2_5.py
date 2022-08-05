
class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, x):
        if type(x) == str and len(x) in range(2, 101):
            self.__model = x
