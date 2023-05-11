class PhoneNumber:
    def __init__(self, number: str):
        self.number = number.replace(" ", "")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.number}')"

    def __str__(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"


phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))

phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))

phone1 = PhoneNumber('9173963385')
phone2 = PhoneNumber('918 396 3389')
phone3 = PhoneNumber('919 333 3344')

print(phone1, phone2, phone3, sep=', ')
print([phone1, phone2, phone3])
