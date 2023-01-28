class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if value.count("@") != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        elif "." not in value[value.index("@"):]:
            raise ValueError("Логин должен содержать символ '.'")
        else:
            self.__login = value


r1 = Registration('qwerty@rambler.ru') # здесь хороший логин
print(r1.login)  # qwerty@rambler.ru

# теперь пытаемся запись плохой логин
r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")

r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")