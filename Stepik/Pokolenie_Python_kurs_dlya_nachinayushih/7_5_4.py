num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10