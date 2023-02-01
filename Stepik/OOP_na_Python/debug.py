class Building:
    def __init__(self, flor):
        self.flor = [None] * flor

    def __setitem__(self, key, value=None):
        self.flor[key] = value

    def __getitem__(self, item):
        return self.flor[item]

    def __delitem__(self, key):
        self.__setitem__(key)


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp'
iron_building[2] = 'Stark'
iron_building[3] = 'SAAAAA'
print(*iron_building)

print(iron_building[2])
del iron_building[2]
print(iron_building[2])
print(*iron_building)
