def triangle(num):
    if num > 0:
        triangle(num - 1)
    print('*' * num)


triangle(5)

