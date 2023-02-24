class Person:
    __slots__ = ("first_name", "last_name", "age")

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"


# Код ниже не удаляйте, он нужен для проверок
arshavin = Person("Andrew", "Arshavin", 35)
assert arshavin.first_name == 'Andrew'
assert arshavin.last_name == 'Arshavin'
assert arshavin.age == 35
print(arshavin)

mg = Person("Max", "Galkin", 44)
assert mg.first_name == 'Max'
assert mg.last_name == 'Galkin'
assert mg.age == 44
print(mg)

try:
    arshavin.city = 'SPB'
except AttributeError:
    print('Нельзя создавать новые атрибуты')
