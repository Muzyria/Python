def alternating_sequence(count=None):
    number = 1
    if count is None:
        while True:
            if number % 2 == 0:
                yield number * -1
            else:
                yield number
            number += 1
    else:
        for number in range(1, count + 1):
            if number % 2 == 0:
                yield number * -1
            else:
                yield number


generator = alternating_sequence()
print(next(generator))
print(next(generator))

generator = alternating_sequence(10)
print(*generator)
