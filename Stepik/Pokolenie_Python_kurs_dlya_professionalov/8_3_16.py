def to_binary(number):
    if number // 2 == 0:
        return str(number % 2)
    else:
        return str(to_binary(number // 2)) + str(number % 2)


print(to_binary(15))
print(to_binary(0))
print(to_binary(1))
