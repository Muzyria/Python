class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")    


class Bus(Vehicle):
    pass    



bus_99 = Bus("Ikarus", 66, 124567)
bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"