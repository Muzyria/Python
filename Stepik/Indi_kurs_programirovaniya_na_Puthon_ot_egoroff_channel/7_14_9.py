def repeater(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner


@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого распечатается две строки со значением 14
multiply(5, 3) # после этого распечатается две строки со значением 15
