def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))
