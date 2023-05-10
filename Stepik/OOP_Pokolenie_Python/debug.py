class ElectricCar:
    status = True

    def disable(self):
        self.__class__.status = False


car1 = ElectricCar()
car2 = ElectricCar()

print(car1.status, car2.status)

car1.disable()

print(car1.status, car2.status)