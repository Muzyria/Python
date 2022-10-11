def is_power(n):
    if n < 2:
        if n == 1:
            return True
        return False
    else:
        return is_power(n / 2)


print(is_power(512))
print(is_power(15))
print(is_power(1))
