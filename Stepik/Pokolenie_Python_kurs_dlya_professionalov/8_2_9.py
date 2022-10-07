def triangle(num):
    if num > 0:
        print(f'*' * num)
        triangle(num - 1)


triangle(5)
