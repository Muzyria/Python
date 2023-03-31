def double_it(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return inner


@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)
@double_it
def get_sum(*args):
    return sum(args)

res = get_sum(1, 2, 3, 4, 5)
print(res) # печатает 30
