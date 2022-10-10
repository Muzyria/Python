def number_of_frogs(year, frogs=77):
    if year == 1:
        return frogs
    else:
        return (number_of_frogs(year - 1) - 30) * 3


print(number_of_frogs(2))
print(number_of_frogs(1))
print(number_of_frogs(10))
