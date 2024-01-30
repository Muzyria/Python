

class SortKey:
    def __init__(self, *args):
        self.args = tuple(args)

    def __call__(self, obj):
        print("Экземпляр класса User -->", obj)
        print("Словарь с атрибутами -->", obj.__dict__)
        print("Название/я атрибута --->>>", tuple(atr for atr in obj.__dict__))
        print("Значение/я атрибута/ов переданных в key=SortKey(...,...))) СПОСОБ №1 --->>>",
              tuple(obj.__getattribute__(i) for i in self.args))
        print("Значение/я атрибута/ов переданных в key=SortKey(...,...))) СПОСОБ №2  --->>>",
              tuple(obj.__dict__[i] for i in self.args))
        print()
        return "ТЕСТ"


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

# print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
# print(sorted(users, key=SortKey('age')))
# print(sorted(users, key=SortKey('age', 'name')))
