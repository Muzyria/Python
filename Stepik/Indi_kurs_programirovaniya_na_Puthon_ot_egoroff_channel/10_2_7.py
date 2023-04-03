def my_range_gen(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError(f"my_range_gen() takes 1-3 positional arguments but {len(args)} were given")

    if step == 0:
        return

    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return

    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        yield i
        i += step





