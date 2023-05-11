class ElectricCar:
    def __new__(cls, *args, **kwargs):
        print('Вызов метода __new__()')
        return object.__new__(cls)

    def __init__(self, color):
        print('Вызов метода __init__()')
        self.color = color


car = ElectricCar('yellow')
print(car.color)