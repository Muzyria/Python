def is_integer(x):
    if x.startswith('-'):
        x = x.replace('-', '', 1)
    return x.isdigit()
