class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if "@" not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        if "." not in value[value.index("@"):]:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = value


r1 = Registration('qwerty@rambler.ru') # здесь хороший логин
print(r1.login)  # qwerty@rambler.ru

# теперь пытаемся запись плохой логин


  

