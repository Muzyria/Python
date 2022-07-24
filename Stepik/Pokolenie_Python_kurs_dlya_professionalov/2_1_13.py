
from re import L


def choose_plural(amount, declensions):
    last_digit = amount % 10
    before_last_digit = (amount // 10) % 10
     
    


print(choose_plural(11, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))