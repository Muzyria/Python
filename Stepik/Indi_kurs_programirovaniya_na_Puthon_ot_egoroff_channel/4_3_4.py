a, b = map(int, input().split())
d, c = a, b  # сохраняем исходные данные в новых переменных
while b > 0:
    a, b = b, a % b
NOK = int((c * d) / a)  # произведение исходных данных делим на НОД и приводим к целочисленному значению
print(NOK)