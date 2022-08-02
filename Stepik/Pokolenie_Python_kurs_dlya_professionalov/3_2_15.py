from datetime import date


def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except:
        return False


print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))
print(is_correct(32, 10, 2021))
