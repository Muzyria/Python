
class Car:
    def __init__(self, model, year, engine_size, price, mileage):
        self.model = model
        self.year = year
        self.engine_size = engine_size
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        print(f'Характеристики автомобиля \nмодель - {self.model},\nгод выпуска - {self.year},\nобъем двигателя - {self.engine_size}, '
              f'\nцена - {self.price},\nпробег - {self.mileage},\nколичество колес - {self.wheels}')
        print()


class Track(Car):
    def __init__(self, model, year, engine_size, price, mileage):
        super().__init__(model, year, engine_size, price, mileage)
        self.wheels = 8

    def description(self):
        print(f'Характеристики грузовика\nмодель - {self.model},\nгод выпуска - {self.year},\nобъем двигателя - {self.engine_size},'
              f'\nцена - {self.price},\nпробег - {self.mileage},\nколичество колес - {self.wheels}')
        print()


my_car = Car('Toyota', 2020, 2000, 15000, 10000)
my_car.description()

my_track = Track('Kamaz', 1990, 4000, 25000, 500000)
my_track.description()
