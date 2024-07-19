class Initialization:
    def __init__(self, capacity: int, food: list):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print("Количество людей должно быть целым числом")


class Vegetarian(Initialization):
    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, Initialization):
            return self.capacity == other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, Initialization):
            return self.capacity < other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, Initialization):
            return self.capacity > other.capacity
        else:
            return f"Невозможно сравнить количество сладкоежек с {other}"


# Ниже располагается код для проверки

p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
