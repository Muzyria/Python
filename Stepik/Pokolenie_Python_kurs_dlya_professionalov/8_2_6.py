def my_rec(start=1, end=100):
    if start <= end:
        print(start)
        my_rec(start + 1)


my_rec()
