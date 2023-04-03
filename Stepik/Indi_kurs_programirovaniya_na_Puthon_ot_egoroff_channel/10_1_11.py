# Создайте генератор
from_10_to_20 = (i for i in range(10, 21))

# Распечатайте три первых значения
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

# выведите все оставшиеся
for value in from_10_to_20:
    print(value)
