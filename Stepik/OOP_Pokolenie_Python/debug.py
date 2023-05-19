class PiggyBank:
    def __init__(self, coins):
        self.coins = coins                         # количество монет в копилке

    def __repr__(self):
        return f'PiggyBank({self.coins})'

    def __add__(self, other):
        print("call __add__")
        return PiggyBank(self.coins + other)       # создаем и возвращаем новый объект

    # def __iadd__(self, other):
    #     print("call __iadd__")
    #     self.coins += other
    #     return self                                # возвращаем измененный объект


bank = PiggyBank(10)

bank += 10
bank += 5

print(bank)