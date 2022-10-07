def print_digits(number):
    if str(number):
        print(str(number)[0])
        print_digits(str(number)[1::])


print_digits(12345)
