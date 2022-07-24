
def likes(names):
    l = len(names)
    if l == 0: return f"Никто не оценил данную запись"
    if l == 1: return f"{names[0]} оценил(а) данную запись"
    if l == 2: return f"{names[0]} и {names[1]} оценили данную запись"
    if l == 3: return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
    return f"{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись"


print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))