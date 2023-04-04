def my_range_gen(*args):
    start, stop, step = 0, 0, 1
    match len(args):
        case 1:
            stop = args[0]
        case 2:
            start, stop = args
        case 3:
            start, stop, step = args

    if step == 0:
        return
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


for i in my_range_gen(4):
    print(i)

# Будет напечатано
# 4
# 6

for i in my_range_gen(8, 5, -2):
    print(i)

# Будет напечатано
# 8
# 7
# 6
