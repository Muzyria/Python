class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if type(i) == int])

    def __str__(self):
        return f"Вектор{tuple(self.values)}" if self.values else "Пустой вектор"

            

v3 = Vector(1)
print(v3)
v1 = Vector(8, 5.5, 1, 2, 3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"            
