class Adder:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y

a = Adder(10)
b = Adder(20)
c = a(5) + b(5)
print(c)