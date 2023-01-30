class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if type(i) == int])

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[i + j for i, j in zip(self.values, other.values)])
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[i * other for i in self.values])
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[i * j for i, j in zip(self.values, other.values)])
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")
