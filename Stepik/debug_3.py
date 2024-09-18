numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]

it_numbers = iter(numbers)

while True:
    try:
        res = next(it_numbers)

    except StopIteration:
        print(res)
        break