class Building:
    def __init__(self, x):
        self.values = list([None]*x)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
            
    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            self.values[key] = None    



iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])

print(iron_building.values)