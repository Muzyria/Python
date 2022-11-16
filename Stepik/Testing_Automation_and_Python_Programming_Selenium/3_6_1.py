
class Car:
    def __init__(self, model, year, engine_size, price, mileage, wheels=4):
        self.model = model
        self.year = year
        self.engine_size = engine_size
        self.price = price
        self.mileage = mileage
        self.wheels = wheels

    def description(self):
        print(f'модель - {self.model},\nгод выпуска - {self.year},\nобъем двигателя - {self.engine_size},'
              f'\nцена - {self.price},\nпробег - {self.mileage},\nколичество колес - {self.wheels}')
        print()


class Track(Car):
    def __int__(self, model, year, engine_size, price, mileage, wheels=8):
        super.__init__(model, year, engine_size, price, mileage)

    def description(self):
        print(f'модель - {self.model},\nгод выпуска - {self.year},\nобъем двигателя - {self.engine_size},'
              f'\nцена - {self.price},\nпробег - {self.mileage},\nколичество колес - {self.wheels}')
        print()


my_car = Car('Toyota', 2020, 2000, 15000, 10000)
my_car.description()

my_track = Car('Kamaz', 1990, 4000, 25000, 500000)
my_track.description()
