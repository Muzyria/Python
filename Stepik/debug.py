

def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, data):
        self._login = data


account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)