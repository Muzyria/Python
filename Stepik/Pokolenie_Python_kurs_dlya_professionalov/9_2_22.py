s = input()
a, b = map(int, input().split())

print(f"Минимальное значение функции {s} на отрезке [{a}; {b}] равно {min(eval(s) for x in range(a, b+1))}")
print(f"Максимальное значение функции {s} на отрезке [{a}; {b}] равно {max(eval(s) for x in range(a, b+1))}")
