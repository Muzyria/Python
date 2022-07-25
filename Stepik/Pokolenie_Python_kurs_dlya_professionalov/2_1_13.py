def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    elif 2 <= amount % 10 <= 4 and amount % 100 not in (12, 13, 14):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'
    

print(choose_plural(512312, ('пример', 'примера', 'примеров')))
print(choose_plural(512312, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(11, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
