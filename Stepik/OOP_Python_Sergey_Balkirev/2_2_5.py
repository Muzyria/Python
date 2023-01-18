
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

"""
class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, x):
        if self.check_model(x):
            self.__model = x

    @classmethod
    def check_model(cls, x):
        if type(x) == str and len(x) in range(2, 101):
            return True
        return False


car = Car()
car.model = "Toyota"
print(car.model)
"""
