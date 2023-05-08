class User:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, data):
        if type(data) == str and data != '' and all(i.isalpha() for i in data):
            self._name = data
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, data):
        if type(data) == int and data in range(0, 111):
            self._age = data
        else:
            raise ValueError('Некорректный возраст')


user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())
