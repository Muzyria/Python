
def dec(func):
    def wrapper(*args, **kwargs):
        args = (str(i).upper() for i in args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*args, **kwargs)
    return wrapper

print = dec(print)



print('hi', 'there', end='!')

