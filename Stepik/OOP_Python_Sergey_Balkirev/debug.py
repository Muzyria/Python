class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old


p = Person("Mishal", 20)
p.set_old(35)
print(p.get_old())
