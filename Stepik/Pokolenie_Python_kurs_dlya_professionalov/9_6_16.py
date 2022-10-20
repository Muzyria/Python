# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     def fun_loop() -> None:
#         for i in range(abs(step)):
#             s = numbers.pop(0)
#             numbers.append(s)
#     if step > 0:
#         numbers.reverse()
#         fun_loop()
#         numbers.reverse()
#     else:
#         fun_loop()

def cyclic_shift(numbers: list[int|float], step: int)-> None:
    for _ in range(abs(step)):
        if step>=0:
            x = numbers.pop(-1)
            numbers.insert(0, x)
        else:
            x = numbers.pop(0)
            numbers.append(x)


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)
# [5, 1, 2, 3, 4]
assert numbers == [5, 1, 2, 3, 4], "не совпадает"

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers, '---------')
# [3, 4, 5, 1, 2]
assert numbers == [3, 4, 5, 1, 2], "не совпадает"

numbers = [234, 235]
cyclic_shift(numbers, 15)
print(numbers)
# [235, 234]
assert numbers == [235, 234], 'не совпадает'
