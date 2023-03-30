def create_accumulator(value=0):
    res = value

    def adder(value):
        nonlocal res
        res += value
        return res

    return adder


summator_1 = create_accumulator(100)
print(summator_1(1)) # печатает 101
print(summator_1(5)) # печатает 106
print(summator_1(2)) # печатает 108

summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7
