class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __setattr__(self, attr, value):
        attr = '+' + attr
        print("__set")
        self.__dict__[attr] = value


cat = Cat('Кемаль', 'Британский')

print(cat.__dict__)