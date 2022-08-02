from datetime import date


def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except:
        return False


count = 0
for d in iter(input, 'end'):
    day, month, year = d.split(".")
    if is_correct(day, month, year):
        count += 1
        print("Корректная")
    else:
        print("Некорректная")

print(count)
