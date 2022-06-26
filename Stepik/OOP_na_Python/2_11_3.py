from string import digits, ascii_uppercase, ascii_lowercase, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password    

    @login.setter
    def login(self, value):
        if "@" not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        if "." not in value[value.index("@"):]:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = value

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False  

    @staticmethod
    def is_include_all_register(password):
        for char in ascii_uppercase:
            if char not in password:
                return False
        for char in ascii_lowercase:
            if char not in password:
                return False 
        return True  

    @staticmethod
    def is_include_only_latin(password):
        for char in ascii_letters:
            if char not in password:
                return False
        return True 

    @staticmethod
    def check_password_dictionary(password):
        pass                  

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError("Пароль должен быть строкой")
        if len(value) <= 4 or len(value) >= 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        self.__password = value    