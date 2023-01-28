from string import ascii_letters

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not type(value) == str:
            raise TypeError("Пароль должен быть строкой")
        elif not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif not self.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not self.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif not self.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif self.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        else:
            self.__password = value

    @staticmethod
    def is_include_digit(value):
        return any(i.isdigit() for i in value)

    @staticmethod
    def is_include_all_register(value):
        return any(i.islower() for i in value) and any(i.isupper() for i in value)

    @staticmethod
    def is_include_only_latin(value):
        return all(i in ascii_letters for i in value if i.isalpha())

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', 'r', encoding='utf-8') as f:
            return value in f.read().split()


r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 43  # raise TypeError("Пароль должен быть строкой")