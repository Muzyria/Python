class Money:
    def __init__(self, d, c):
        self.total_cents = d*100+c
       
    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if type(value) == int and value >= 0:
            self.total_cents = value*100 + self.cents
        else:
            print("Error dollars")   

    @cents.setter
    def cents(self, value):
        if type(value) == int and 0 <= value <= 99 :
            self.total_cents = self.dollars*100 + value
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

"""
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, val):
        if type(val) == int and val >= 0:
            self.total_cents = self.cents + val * 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, val):
        if type(val) == int and 0 <= val < 100:
            self.total_cents = self.total_cents - self.cents + val
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
"""
