def create_accumulator():
    res = 0

    def adder(value):
        nonlocal res
        res += value
        return res

    return adder


summator_1 = create_accumulator()
print(summator_1(1))  # печатает 1
print(summator_1(5))  # печатает 6
print(summator_1(2))  # печатает 8

summator_2 = create_accumulator()
print(summator_2(3))  # печатает 3
print(summator_2(4))  # печатает 7
