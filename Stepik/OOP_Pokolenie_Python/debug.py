class ElectricCar:
    def __init__(self, owner):
        self.owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, str) and owner.isalpha():
            self._owner = owner
        else:
            raise ValueError


car = ElectricCar(['Gvido', 'Elon'])

print(car.owner)