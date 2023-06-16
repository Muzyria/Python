class Validator:
    def __init__(self, obj):
        self._obj = obj

    def is_valid(self):
        pass


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self._obj, (int, float))


validator1 = NumberValidator('beegeek')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())
