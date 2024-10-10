

class FoodInfo:
    def __init__(self, proteins: int | float, fats: int | float, carbohydrates: int | float):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(*tuple([i[0] + i[1] for i in zip(self.__dict__.values(), other.__dict__.values())]))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*tuple([i * other for i in self.__dict__.values()]))
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*tuple([i / other for i in self.__dict__.values()]))
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*tuple([i // other for i in self.__dict__.values()]))
        return NotImplemented



food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

