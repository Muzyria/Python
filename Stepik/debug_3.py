
class Account:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def hash_function(self, password: str) -> int:
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str) -> None:
        if not hasattr(self, "_login"):
            self._login = value
        else:
            raise AttributeError("Изменение логина невозможно")

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = self.hash_function(value)

account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)
