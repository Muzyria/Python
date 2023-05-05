class ElectricCar:
    engine_type = 'electric motor'


car = ElectricCar()

car.color = 'black'

print('engine_type' in ElectricCar.__dict__)
print('color' in ElectricCar.__dict__)
print(car.__dict__)
print(ElectricCar.__dict__)