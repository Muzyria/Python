import sys


print('Ведите корректное математическое выражение (в фортмате 2 + 2)')
for line in sys.stdin:
    try:
        print(f' = {eval(line)}')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except Exception:
        print('Не коректные данные')
