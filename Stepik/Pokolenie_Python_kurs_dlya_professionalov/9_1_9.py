def non_negative_even(number):
    return all(i >= 0 and i % 2 == 0 for i in number)


print(non_negative_even([0, 2, 4, 8, 16]))
# True
