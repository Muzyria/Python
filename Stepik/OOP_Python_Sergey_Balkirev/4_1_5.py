class Animal:
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old

    def get_info(self):
        return f'{self.name}: {self.old}, {", ".join([str(i) for i in self.__dict__.values()][2:])}'


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size


if __name__ == '__main__':
    cat = Cat('кот', 4, 'black', 2.25)
    dog = Dog('пес', 3, 'red', (2, 3))
    print(cat.get_info())
    print(dog.get_info())
