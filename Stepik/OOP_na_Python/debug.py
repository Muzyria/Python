try:
    a = int(input())
    b = int(input())
    print(f"Результат деления a на b: {a/b}")
except (ValueError, ZeroDivisionError):
    print('Введите корректные значения')
