def create_accumulator(total: int | float = 0) -> callable:
    def inner(x: int | float) -> int | float:
        nonlocal total
        total += x
        return total
    return inner


summator_1 = create_accumulator(200)
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))