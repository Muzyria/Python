# import sys
#
#
# print('Ведите корректное математическое выражение (в фортмате 2 + 2)')
# for line in sys.stdin:
#     try:
#         print(f' = {eval(line)}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#     except Exception:
#         print('Не корректные данные')


try:
    a = input('Введите 1-е число ')
    z = input('Введите арифметический знак, один из: +, -, *, / ')
    b = input('Введите 2-е число ')
    print(eval(f'{a}{z}{b}'))
except ZeroDivisionError:
    print('На ноль делить нельзя')
except Exception:
    print('Не корректные данные')
