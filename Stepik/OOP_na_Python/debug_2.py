def quick_power(a: int, n: int) -> int:
    # Вывод состояния параметров
    print(f"State: a={a}, n={n}")

    if n == 0:
        return 1  # Базовый случай: любое число в нулевой степени равно 1
    elif n % 2 == 0:
        half_power = quick_power(a, n // 2)  # Рекурсивный вызов для четного n
        return half_power * half_power
    else:
        return a * quick_power(a, n - 1)  # Рекурсивный вызов для нечетного n

print(quick_power(1, 1000))