class SortKey:
    def __init__(self, *args):
        self.attributes = args
        print(f'init{self.attributes}')

    def __call__(self, obj):
        key = tuple(getattr(obj, attr) for attr in self.attributes)
        print(obj, key)
        return key


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))
