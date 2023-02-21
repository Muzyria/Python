class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return "Weak"
        elif len(self.password) > 11:
            return "Strong"
        else:
            return "Medium"

# Напишите определение класса Password


# Ниже код для проверки методов класса Password

pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')